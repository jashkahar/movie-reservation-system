# Use the official PostgreSQL image as the base image
FROM postgres:17

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=postgresuser
ENV POSTGRES_PASSWORD=pass@123

RUN apt-get update && apt-get install -y postgresql-17-pgagent

# # Copy the SQL file to the initialization directory in the container
# # Make sure the path to the SQL file is relative to the build context
# COPY init_db.sh /docker-entrypoint-initdb.d/init_db.sh

# Expose the PostgreSQL default port
EXPOSE 5432
CMD ["postgres"]