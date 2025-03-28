from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PatientBase(BaseModel):
    age: int = Field(..., ge=0, le=120)
    bmi: float = Field(..., ge=0, le=70)
    glucose: float = Field(..., ge=0, le=300)
    blood_pressure: float = Field(..., ge=0, le=200)
    skin_thickness: float = Field(..., ge=0, le=100)
    insulin: float = Field(..., ge=0, le=1000)
    pregnancies: int = Field(..., ge=0, le=20)
    diabetes_pedigree: float = Field(..., ge=0, le=3)

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    diabetes_prediction: Optional[float] = None
    diabetes_risk: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True