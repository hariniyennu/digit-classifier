# Use official lightweight Python image (Python 3.10)
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 10000

# Command to run your Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
