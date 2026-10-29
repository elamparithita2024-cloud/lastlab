# Use an official lightweight Python runtime
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all local project files into the container workspace
COPY . /app

# Install the testing tool so the container can execute tests if needed
RUN pip install pytest

# Command to execute your billing application when the container starts
CMD ["python", "app.py"]
