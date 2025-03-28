from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from schemas.prediction import DiabetesPredictionInput, PredictionOutput
from security import get_current_user
import sys
import os

# Add ml_core to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ml_core'))
from models.diabetes_model import DiabetesPredictor

router = APIRouter(prefix="/predictions", tags=["predictions"])
diabetes_predictor = DiabetesPredictor()

@router.post("/diabetes", response_model=PredictionOutput)
async def predict_diabetes(
    data: DiabetesPredictionInput,
    current_user: Annotated[str, Depends(get_current_user)]
):
    """Predict diabetes risk for a patient"""
    try:
        # Convert input data to dict for prediction
        patient_data = data.dict()
        
        # Make prediction
        result = diabetes_predictor.predict(patient_data)
        
        return {
            "success": True,
            "prediction": result['prediction'],
            "probability": result['probability'],
            "risk_level": result['risk_level'],
            "model": "RandomForestClassifier"
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction failed: {str(e)}"
        )