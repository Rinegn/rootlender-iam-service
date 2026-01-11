from fastapi import FastAPI
from app.api.health_routes import router as health_router

app = FastAPI(title="RootLender IAM Service")

app.include_router(health_router)
