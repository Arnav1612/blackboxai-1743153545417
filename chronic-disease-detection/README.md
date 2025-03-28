# Chronic Disease Detection System

A full-stack application for predicting chronic disease risks using machine learning.

## Features

- **Backend API** (FastAPI)
  - User authentication (JWT)
  - Diabetes risk prediction endpoint
  - Database integration (PostgreSQL)
  
- **Frontend** (Vue.js + Tailwind CSS)
  - Responsive UI
  - Patient data input form
  - Risk visualization
  - User authentication flows

- **Machine Learning Core**
  - Pre-trained diabetes prediction model
  - Data preprocessing pipeline
  - Model interpretability features

## Project Structure

```
chronic-disease-detection/
├── backend/               # FastAPI backend
│   ├── database/          # Database models and operations
│   ├── routes/            # API endpoints
│   ├── schemas/           # Pydantic models
│   ├── main.py            # Application entry point
│   └── requirements.txt   # Python dependencies
│
├── frontend/              # Vue.js frontend
│   ├── src/               # Source files
│   │   ├── assets/        # Static assets
│   │   ├── components/    # Vue components
│   │   ├── router/        # Vue router config
│   │   ├── store/         # Vuex store
│   │   ├── views/         # Page components
│   │   ├── App.vue        # Main app component
│   │   └── main.js        # App entry point
│   ├── package.json       # Frontend dependencies
│   └── requirements.txt   # Node environment setup
│
├── ml_core/               # Machine learning components
│   ├── data_processing/   # Data cleaning and prep
│   ├── models/            # Trained models
│   └── requirements.txt   # ML dependencies
│
└── docs/                  # Documentation
    └── DEVELOPER_SETUP.md # Setup instructions
```

## Setup

### Backend

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Install Node.js (v16+)

2. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

3. Run the development server:
   ```bash
   npm run serve
   ```

## License

MIT