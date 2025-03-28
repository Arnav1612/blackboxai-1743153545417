from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    bmi = Column(Float)
    glucose = Column(Float)
    blood_pressure = Column(Float)
    skin_thickness = Column(Float)
    insulin = Column(Float)
    pregnancies = Column(Integer)
    diabetes_pedigree = Column(Float)
    diabetes_prediction = Column(Float)
    diabetes_risk = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)