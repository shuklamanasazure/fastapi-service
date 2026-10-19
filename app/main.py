from fastapi import FastAPI  # Import the FastAPI application framework
from pydantic import BaseModel  # Define validated response models
import os  # Read runtime configuration from environment variables

app = FastAPI(title="FastAPI Service")  # Create the API application

class AppInfo(BaseModel):  # Define the response schema
    name: str  # Application name
    environment: str  # Deployment environment

@app.get("/api/v1/info", response_model=AppInfo)  # Register an information endpoint
def get_info():
    return AppInfo(  # Return structured application metadata
        name="fastapi-service",
        environment=os.getenv("APP_ENV", "local"),  # Use environment configuration
    )

@app.get("/api/v1/healthz")  # Register a lightweight health endpoint
def health():
    return {"status": "ok"}  # Return a simple health response