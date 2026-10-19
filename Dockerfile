FROM python:3.12-slim                 
# Use a small Python runtime base image

#ENV PYTHONDONTWRITEBYTECODE=1          
# Avoid writing Python bytecode files
#ENV PYTHONUNBUFFERED=1                 
# Send logs directly to container output

WORKDIR /app                           
# Set the application working directory

COPY requirements.txt .               
# Copy only runtime dependencies first
RUN pip install --no-cache-dir -r requirements.txt  
# Install dependencies

#RUN useradd --create-home --uid 10001 appuser  
# Create a non-root runtime user

COPY . .
#COPY --chown=appuser:appuser app/ ./app/  
# Copy application source with ownership

#USER 10001                              
# Run the process as a non-root user

EXPOSE 8001                             
# Document the application port

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
# Start Uvicorn and listen on all container interfaces