#!/bin/bash
set -e

# Create the fastq directory if it doesn't exist
mkdir -p fastq

process_metadata() {
    local csv_file=$1

    # Skip the header and read each line from the CSV file
    sed '1d' "$csv_file" | while IFS=',' read -r accn name
    do
        # Replace spaces and hyphens with underscores in the name
        name=$(echo "$name" | tr ' -' '__')

        # Download the FASTQ file using fasterq-dump
        fasterq-dump "$accn"

        # Rename and compress the downloaded FASTQ file
        head -n 200000 "${accn}.fastq" | gzip > "fastq/${name}_R1.fastq.gz"
        rm "${accn}.fastq"
    done
}

# Process metadata files
process_metadata ./data/PRJNA362531_metadata.csv
process_metadata ./data/PRJNA362529_metadata.csv
