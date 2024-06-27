import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS


def load_data(file_path):
    """
    Load the beta diversity data from a given file path.

    Parameters:
    file_path (str): Path to the beta diversity summary file.

    Returns:
    pd.DataFrame: DataFrame containing the beta diversity data.
    """
    return pd.read_csv(file_path, sep='\t')


def extract_distance_data(df):
    """
    Extract the relevant columns for the distance matrix.

    Parameters:
    df (pd.DataFrame): DataFrame containing the beta diversity data.

    Returns:
    pd.DataFrame: DataFrame with sample1, sample2, and braycurtis columns.
    """
    df['sample1'] = df['label'].str.strip()
    df['sample2'] = df['comparison'].str.strip()
    return df[['sample1', 'sample2', 'braycurtis']]


def create_distance_matrix(distance_data):
    """
    Create a distance matrix from the distance data.

    Parameters:
    distance_data (pd.DataFrame): DataFrame containing sample1, sample2,
        and braycurtis columns.

    Returns:
    np.ndarray: Distance matrix.
    list: List of unique sample names.
    """
    samples = sorted(set(distance_data
                         ['sample1']).union(set(distance_data['sample2'])))
    sample_index = {sample: idx for idx, sample in enumerate(samples)}

    n_samples = len(samples)
    distance_matrix = np.zeros((n_samples, n_samples))

    for _, row in distance_data.iterrows():
        i, j = sample_index[row['sample1']], sample_index[row['sample2']]
        distance_matrix[i, j] = distance_matrix[j, i] = row['braycurtis']

    return distance_matrix, samples


def assign_color(sample_name, conditions):
    """
    Assign a color to a sample based on its condition.

    Parameters:
    sample_name (str): Name of the sample.
    conditions (dict): Dictionary mapping conditions to colors.

    Returns:
    str: Color assigned to the sample.
    """
    for condition in conditions:
        if condition in sample_name.lower():
            return conditions[condition]
    return 'gray'


def assign_shape(sample_name):
    """
    Assign a shape to a sample based on its type.

    Parameters:
    sample_name (str): Name of the sample.

    Returns:
    str: Shape assigned to the sample ('o' for DNA, '^' for RNA.
    """
    if 'dna' in sample_name.lower():
        return 'o'  # Circle
    elif 'rna' in sample_name.lower():
        return '^'  # Triangle
    return 's'  # Square for any other cases


def plot_pcoa(coords, samples, colors, shapes, conditions):
    """
    Plot the PCoA with color-coded and shape-coded points.

    Parameters:
    coords (np.ndarray): Coordinates from MDS.
    samples (list): List of sample names.
    colors (list): List of colors for each sample.
    shapes (list): List of shapes for each sample.
    conditions (dict): Dictionary mapping conditions to colors.
    """
    plt.figure(figsize=(12, 10))

    for (x, y), color, shape in zip(coords, colors, shapes):
        plt.scatter(x, y, c=color, marker=shape, s=100)

    legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
                                  markerfacecolor=color, markersize=10,
                                  label=condition)
                       for condition, color in conditions.items()]

    legend_elements += [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='black',
                   markersize=10, label='DNA'),
        plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='black',
                   markersize=10, label='RNA')
    ]

    plt.legend(handles=legend_elements, title="Conditions and Types")
    plt.xlabel('PCoA1')
    plt.ylabel('PCoA2')
    plt.title('Principal Coordinates Analysis (PCoA) with Grouped Samples')
    plt.grid(True)
    plt.show()


def main():
    # Load the data
    beta_diversity_path = 'beta-diversity.97.summary'
    beta_diversity_df = load_data(beta_diversity_path)

    # Print column names for debugging
    print("Column names in beta_diversity_df:", beta_diversity_df.columns)

    # Extract the relevant columns for the distance matrix
    distance_data = extract_distance_data(beta_diversity_df)

    # Create the distance matrix
    distance_matrix, samples = create_distance_matrix(distance_data)

    # Perform PCoA using MDS (Multidimensional Scaling)
    mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
    coords = mds.fit_transform(distance_matrix)

    # Define the conditions for each sample
    conditions = {
        'fresh_irrigated': 'blue',
        'fresh_rainfed': 'orange',
        'dreid_irrigated': 'green',
        'dreid_rainfed': 'red',
        'incubated_irrigated': 'purple',
        'incubated_rainfed': 'brown',
        'reincubated_irrigated': 'pink',
        'reincubated_rainfed': 'olive'
    }

    # Assign colors and shapes to each sample
    colors = [assign_color(sample, conditions) for sample in samples]
    shapes = [assign_shape(sample) for sample in samples]

    # Plot the PCoA with color-coded and shape-coded points
    plot_pcoa(coords, samples, colors, shapes, conditions)


if __name__ == "__main__":
    main()
