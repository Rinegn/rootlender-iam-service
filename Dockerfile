FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Python runtime safety
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (curl for healthchecks, optional but useful)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app app

# Expose service port
EXPOSE 8000

# Start FastAPI using Uvicorn (LONG-RUNNING PROCESS)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
