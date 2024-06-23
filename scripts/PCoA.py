import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS

# Load the data
beta_diversity_path = 'beta-diversity.97.summary'
beta_diversity_df = pd.read_csv(beta_diversity_path, sep='\t')

# Print column names for debugging
print("Column names in beta_diversity_df:", beta_diversity_df.columns)

# Extract the relevant columns for the distance matrix
beta_diversity_df['sample1'] = beta_diversity_df['label'].str.strip()
beta_diversity_df['sample2'] = beta_diversity_df['comparison'].str.strip()
distance_data = beta_diversity_df[['sample1', 'sample2', 'braycurtis']]

# Get the unique sample names
samples = sorted(set(distance_data['sample1']).union(set(distance_data['sample2'])))
sample_index = {sample: idx for idx, sample in enumerate(samples)}

# Initialize the distance matrix
n_samples = len(samples)
distance_matrix = np.zeros((n_samples, n_samples))

# Fill in the distance matrix
for _, row in distance_data.iterrows():
    i, j = sample_index[row['sample1']], sample_index[row['sample2']]
    distance_matrix[i, j] = distance_matrix[j, i] = row['braycurtis']

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

def assign_color(sample_name):
    for condition in conditions:
        if condition in sample_name.lower():
            return conditions[condition]
    return 'gray'

def assign_shape(sample_name):
    if 'dna' in sample_name.lower():
        return 'o'  # Circle
    elif 'rna' in sample_name.lower():
        return '^'  # Triangle
    return 's'  # Square for any other cases

# Assign colors and shapes to each sample based on their conditions and type
colors = [assign_color(sample) for sample in samples]
shapes = [assign_shape(sample) for sample in samples]

# Plot the PCoA with color-coded and shape-coded points
plt.figure(figsize=(12, 10))

# Plot each sample with the appropriate color and shape
for (x, y), color, shape in zip(coords, colors, shapes):
    plt.scatter(x, y, c=color, marker=shape, s=100)

# Create a custom legend for conditions
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=condition)
                   for condition, color in conditions.items()]

# Create a custom legend for sample types
legend_elements += [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=10, label='DNA'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='black', markersize=10, label='RNA')
]

plt.legend(handles=legend_elements, title="Conditions and Types")
plt.xlabel('PCoA1')
plt.ylabel('PCoA2')
plt.title('Principal Coordinates Analysis (PCoA) with Grouped Samples')
plt.grid(True)
plt.show()

