#!/bin/bash

echo "Creating adaptive conda environment. This will take some time (minutes)"

# Ensure Conda is initialized for the current shell
eval "$(conda shell.bash hook)"

# Create the Conda environment
conda env create -f conda_env.yml -n stocks 

# Clean up unnecessary files
conda clean -a --yes

# Initialize bashrc
conda init

# display environments
conda info --envs

# Add 'conda activate adaptive' to ~/.bashrc if not already present
if ! grep -q "conda activate stocks" ~/.bashrc; then
    echo "Adding 'conda activate stocks' to ~/.bashrc"
    echo -e "\n# Activate the stocks conda environment by default\nconda activate stocks" >> ~/.bashrc
fi

# Activate the environment
conda activate stocks

echo "Setup completed successfully!"
