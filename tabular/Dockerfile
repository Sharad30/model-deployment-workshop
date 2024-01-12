# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local src directory contents into the container at /app
COPY . /app

COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port Flask and Streamlit will run on
EXPOSE 5000 8501

# Define the command to run on container start
CMD ["sh", "start.sh"]
