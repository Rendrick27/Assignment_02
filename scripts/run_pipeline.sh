#!/bin/bash

# Define variables
USER=$(whoami)
READS="/home/$USER/Documents/GitHub/Assignment_02/fastq/*.fastq.gz"
REFERENCE_ALN="/home/$USER/Documents/GitHub/Assignment_02/silva.seed_v138_1.align"
REFERENCE_TAX="/home/$USER/Documents/GitHub/Assignment_02/databases/silva.seed_v138_1.tax"
OUTDIR="/home/$USER/Documents/GitHub/Assignment_02/Results_RNA"
CPUS=2

# Run the pipeline
nextflow run Pipeline-16S -profile docker --reads "$READS" --referenceAln "$REFERENCE_ALN" --referenceTax "$REFERENCE_TAX" --outdir "$OUTDIR" --cpus "$CPUS"
