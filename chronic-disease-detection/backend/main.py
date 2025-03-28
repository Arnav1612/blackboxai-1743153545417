import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes import prediction, auth
from security import oauth2_scheme, get_current_active_user
from database import models, session
from database.session import engine
import os

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Chronic Disease Detection API",
    description="API for predicting chronic disease risks",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(prediction.router)

@app.get("/")
async def root():
    return {"message": "Chronic Disease Detection API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}

@app.get("/secure-route/")
async def secure_route(current_user: str = Depends(get_current_active_user)):
    return {"message": "This is a secure route", "user": current_user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
