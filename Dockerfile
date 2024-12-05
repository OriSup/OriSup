# Use the official Python 3.11 image
FROM python:3.11-slim

# Set environment variables to avoid Streamlit interactive issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir streamlit python-dotenv

# Install a lightweight HTTP server for serving static files
RUN apt-get update && apt-get install -y \
    python3 && \
    apt-get clean

# Expose ports for Streamlit (8501) and HTTP server (8000)
EXPOSE 8501 8000

# Create a script to start both servers
RUN echo '#!/bin/bash\n\
python3 -m http.server 8000 --directory /app/landingpage &\n\
streamlit run /app/streamlit_app.py\n' > /app/start.sh && chmod +x /app/start.sh

# Set the entry point to run the start script
ENTRYPOINT ["/bin/bash", "/app/start.sh"]
