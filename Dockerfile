# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy all files into the container
COPY . .

# Command to run the Flask app
CMD ["python", "app.py"]
