# Use an official Python runtime as a parent image
FROM python:3.10-slim-bullseye

# Install required system dependencies and MySQL client development files
RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential default-libmysqlclient-dev \
  && pip install --no-cache-dir --upgrade pip

# Set the environment variables for MySQL client
ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"
ENV ARCHFLAGS="-arch x86_64"

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install the required packages
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt

# Copy the rest of the application files
COPY . /app

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run your Flask application
CMD ["python3", "server.py"]
