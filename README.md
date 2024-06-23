# MethanoReplica: Reproducing Methanogenic Microbial Responses

## Description
MethanoReplica is a project dedicated to replicating and validating the results of the study "Response of Methanogenic Microbial Communities to Desiccation Stress in Flooded and Rain-Fed Paddy Soil from Thailand."

![Pipeline](./extras/pictures/pipeline.png)

## Features
* Download original Bioproject files into fastq;
* Generates:
    * bi-clustered heatmap;
    * scatter plot of OTUs abundance vs prevalence
    * barplot of relative taxonomy composition at Phylum level for each sample
* PCoA graph.

## Requirements
* <a href= "https://github.com/ncbi/sra-tools?tab=readme-ov-file">Sra-tools (3.11)</a>
* <a href= "https://www.nextflow.io/">Nextflow (24.04.2.5914)</a>
* <a href= "https://www.java.com/en/">Java (11.0.23)</a>
* <a href= "https://www.python.org/">Python (3.11.5)</a>
    * <a href= "https://www.python.org/">pandas (2.2.2)</a>
    * <a href= "https://www.python.org/">numpy (1.26.4)</a>
    * <a href= "https://www.python.org/">matplotlib (3.9.0)</a>
    * <a href= "https://www.python.org/">scikit-learn (1.5.0)</a>
* <a href= "https://www.docker.com/">Docker (26.1.4)</a>
* <a href= "https://metagenomics-pipelines.readthedocs.io/en/latest/pipeline_16S.html">Others</a>
  
## Installation
```bash
# Download the project
wget https://github.com/Rendrick27/Assignment_02/archive/refs/heads/main.zip

# Unzip the folder
unzip main.zip
```

## Usage
```bash
# Navigate to the directory
cd main.zip
```

### Scripts
* process_metadata.sh -> Downloads the Bioproject in fastq files with the following formart

```bash
DNA_dreid_irrigated_rep1_R1.fastq.gz
#This script must be runned in the main folder
```
* diversity_mapper_PCoA.py -> Creates a PCoA graph based on results from the nextflow pipeline (It requires the beta-diversity.97.summary file)
```bash
#This script must be runned in folder of results>postprocessing
```

* run_pipeline.sh -> Runs the nextflow pipeline
```bash
#This script must be runned in folder of nextflow
```

## Credits
### Original 16s Pipeline
* <p> <a href= "https://github.com/hawaiidatascience/metaflowmics"> 
hawaiidatascience
 </a> </p>

### Students
* <p> <a href= "https://github.com/Joana204"> Joana Caetano- 202200646 </a> </p>
* <p> <a href= "https://github.com/LaraEvangelista"> Lara Evangelista - 202200655 </a> </p>
* <p> <a href= "https://github.com/LucasTerlica"> Lucas Terlica - 202200239 </a> </p>
* <p> <a href= "https://github.com/Rendrick27"> Rendrick Carreira - 201901365 </a> </p>

## License
GPLv3
