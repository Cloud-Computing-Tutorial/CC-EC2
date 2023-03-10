FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install streamlit

# Copy the application code
COPY source /app

# Set the working directory
WORKDIR /app

USER nobody

# Run the application
CMD ["streamlit", "run", "main.py"]
