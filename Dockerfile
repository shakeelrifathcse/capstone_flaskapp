FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

