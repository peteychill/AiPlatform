FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Run migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && python createadmin.py && python manage.py runsslserver 0.0.0.0:5006"]
