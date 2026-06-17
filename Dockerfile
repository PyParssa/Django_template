# Use an official lightweight Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory, it is a working directory in side container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run the application using Gunicorn, config is where is wsgi file sitting
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
