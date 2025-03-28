import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

class DataCleaner:
    def __init__(self):
        self.imputer = SimpleImputer(strategy='median')
        self.scaler = StandardScaler()
        
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and preprocess patient data"""
        # Handle missing values
        df = self._handle_missing_values(df)
        
        # Remove outliers
        df = self._remove_outliers(df)
        
        # Normalize features
        df = self._normalize_features(df)
        
        return df
    
    def _handle_missing_values(self, df):
        return pd.DataFrame(self.imputer.fit_transform(df), columns=df.columns)
    
    def _remove_outliers(self, df):
        # Remove values beyond 3 standard deviations
        return df[(np.abs(df - df.mean()) <= (3 * df.std())).all(axis=1)]
    
    def _normalize_features(self, df):
        return pd.DataFrame(self.scaler.fit_transform(df), columns=df.columns)