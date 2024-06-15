#!/bin/bash

# Define variables
USER=$(whoami)
READS="/home/$USER/project/fastq/*.fastq.gz"
REFERENCE_ALN="/home/$USER/project/databases/silva.seed_v138_1.align"
REFERENCE_TAX="/home/$USER/project/databases/silva.seed_v138_1.tax"
OUTDIR="/home/$USER/drought_results"
CPUS=2

# Run the Nextflow pipeline
nextflow run Pipeline-16S -profile docker --reads "$READS" --referenceAln "$REFERENCE_ALN" --referenceTax "$REFERENCE_TAX" --outdir "$OUTDIR" --cpus "$CPUS"

