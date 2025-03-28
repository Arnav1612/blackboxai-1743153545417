import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import joblib
import os

class DiabetesPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model_path = 'models/diabetes_model.joblib'
        
    def train(self, data_path: str):
        """Train diabetes prediction model"""
        df = pd.read_csv(data_path)
        X = df.drop('Outcome', axis=1)
        y = df['Outcome']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred)
        
        print(f"Model trained with accuracy: {acc:.2f}, ROC AUC: {roc_auc:.2f}")
        
        # Save model
        os.makedirs('models', exist_ok=True)
        joblib.dump(self.model, self.model_path)
        
    def predict(self, patient_data: dict) -> dict:
        """Make prediction for a single patient"""
        if not os.path.exists(self.model_path):
            raise ValueError("Model not trained yet")
            
        model = joblib.load(self.model_path)
        df = pd.DataFrame([patient_data])
        proba = model.predict_proba(df)[0][1]
        
        return {
            'prediction': int(proba > 0.5),
            'probability': float(proba),
            'risk_level': self._get_risk_level(proba)
        }
        
    def _get_risk_level(self, probability: float) -> str:
        if probability < 0.3:
            return 'Low'
        elif probability < 0.7:
            return 'Medium'
        else:
            return 'High'