#!/bin/bash

# Exit if any command fails
set -e

# Step 1: Install python venv module
echo "Installing python3.11-venv..."
sudo apt install python3.11-venv

echo "Creating Python virtual environment..."
python3 -m venv .venv

# Step 2: Install dependencies
echo "Installing dependencies from requirements.txt..."
source .venv/bin/activate
python3 -m pip install -r requirements.txt
deactivate

# Step 3: Grant access to folders
echo "Changing permissions for notebooks and data folders..."
sudo chmod 777 notebooks
sudo chmod 777 data

# Step 4: Spin up docker container
echo "Starting Docker containers..."
docker compose up -d

# Step 5: Copy files to Hadoop
echo "Copying files to Hadoop..."
docker exec -it resourcemanager /bin/bash -c "\
    hadoop fs -mkdir /energy-data && \
    cd /opt/energy-data && \
    hadoop fs -put owid-energy-data.csv /energy-data/ && \
    hadoop fs -ls /energy-data/"

# Step 6: Check Jupyter server
docker exec spark-notebook jupyter server list

# Step 7: Create database
echo "Creating Hive database..."
docker exec -it hive-server hive -e "CREATE DATABASE wes"


echo "Setup complete!"
