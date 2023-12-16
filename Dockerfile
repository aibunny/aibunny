# Use the official Python base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt ./

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Install project dependencies with pip within the virtual environment
RUN pip install -r requirements.txt

# Copy the project code to the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the Daphne server port
EXPOSE 8000

# Use Daphne to serve the Django ASGI application
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "simplex.wsgi:application"]