# Use the official Python image as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/app.py
COPY templates /app/templates
COPY static /app/static

# Install Flask (and other dependencies if required)
RUN pip install --no-cache-dir flask

# Expose the port your app is running on (port 4949 as specified in app.py)
EXPOSE 4949

# Define the command to run your app
CMD ["python", "app.py"]
