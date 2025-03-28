from pydantic import BaseModel, Field, validator
from typing import Optional

class DiabetesPredictionInput(BaseModel):
    """Input schema for diabetes prediction"""
    pregnancies: int = Field(..., ge=0, le=20, description="Number of pregnancies")
    glucose: float = Field(..., ge=0, le=300, description="Glucose level in mg/dL")
    blood_pressure: float = Field(..., ge=0, le=200, description="Blood pressure in mmHg")
    skin_thickness: float = Field(..., ge=0, le=100, description="Skin thickness in mm")
    insulin: float = Field(..., ge=0, le=1000, description="Insulin level in μU/mL")
    bmi: float = Field(..., ge=0, le=70, description="Body mass index")
    diabetes_pedigree: float = Field(..., ge=0, le=3, description="Diabetes pedigree function")
    age: int = Field(..., ge=0, le=120, description="Age in years")

    @validator('*', pre=True)
    def replace_empty_with_none(cls, v):
        return None if v == "" else v

class PredictionOutput(BaseModel):
    """Output schema for prediction results"""
    success: bool
    prediction: int
    probability: float
    risk_level: str
    model: str
    explanation: Optional[str] = None
    feature_importance: Optional[dict] = None