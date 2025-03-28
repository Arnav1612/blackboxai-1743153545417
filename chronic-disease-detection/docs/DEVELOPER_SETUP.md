# Developer Setup Guide

## Prerequisites
- Python 3.9+
- Node.js 16+ (for frontend)
- PostgreSQL 13+
- Redis 6+

## Installation

1. Clone the repository
2. Set up virtual environments:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install requirements:
```bash
cd ml_core && pip install -r requirements.txt
cd ../backend && pip install -r requirements.txt
```

4. Set up frontend:
```bash
cd ../frontend
npm install
```

## Configuration
Create `.env` file with:
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/chronic_disease_detection
REDIS_URL=redis://localhost:6379
```

## Running the Application
1. Start the backend:
```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend:
```bash
cd frontend
npm run serve