#!/bin/bash

# Define variables

# Copy the SQL file to the container
echo "Copying $SQL_FILE to $CONTAINER_NAME..."
cp ./alldatabases.sql moviereservationpostgresdb:/tmp/alldatabases.sql

# Execute the SQL file inside the container
echo "Initializing the database with $SQL_FILE..."
psql -U postgres -f /tmp/alldatabases.sql

echo "Database initialization completed!"
