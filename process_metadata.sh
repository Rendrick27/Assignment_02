#!/bin/bash
set -e

# Create folders if they don't exist
mkdir -p fastq
mkdir -p databases

# Download and extract the SILVA database
wget https://mothur.s3.us-east-2.amazonaws.com/wiki/silva.seed_v138_1.tgz -O silva.seed_v138_1.tgz
cd databases
tar xfv ../silva.seed_v138_1.tgz
rm ../silva.seed_v138_1.tgz
cd ..

# Function to process metadata CSV files
process_metadata() {
    local csv_file=$1

    # Skip the header and read each line from the CSV file
    sed '1d' "$csv_file" | while IFS=',' read -r accn name
    do
        # Replace spaces and hyphens with underscores in the name
        name=$(echo "$name" | tr ' -' '__')

        # Download the FASTQ file using fasterq-dump with your email address
        fasterq-dump "$accn"

        # Rename and compress the downloaded FASTQ file
        gzip -c "${accn}.fastq" | head -n 200000 > "fastq/${name}_R1.fastq.gz"
        rm "${accn}.fastq"
    done
}

# Process the metadata CSV files
process_metadata ./data/PRJNA362531_metadata.csv
process_metadata ./data/PRJNA362529_metadata.csv

