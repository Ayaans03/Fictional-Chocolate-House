# Using official Python image from Docker
FROM python:3.9-slim

# Seting working directory in the Docker container
WORKDIR /app

# Coping all files into the Docker container
COPY . .

# Command to run app.py
CMD ["python", "app.py"]
