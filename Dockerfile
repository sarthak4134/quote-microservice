# Use an official lightweight Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the dependency file into the container
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Inform Docker that the container listens on port 5000
EXPOSE 5000

# Define the command to run your application when the container starts
CMD ["python", "app.py"]