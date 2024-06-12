# Use the official Python image as a base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the Python script and requirements.txt file into the container
COPY bot.py .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Run the Python script
CMD ["python", "bot.py"]
