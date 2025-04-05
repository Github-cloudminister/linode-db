# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY app.py .

# Install required packages
RUN pip install --no-cache-dir flask psycopg2-binary

# Expose port 3000 for the Flask server
EXPOSE 3000

# Run the app
CMD ["python", "app.py"]
