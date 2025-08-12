from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb
import numpy as np
import json

app = FastAPI()

# Charger le modèle
booster = xgb.Booster()
booster.load_model("xgb_model.model") 

class InputData(BaseModel):
    features: list  # liste de valeurs numériques

@app.post("/predict")
def predict(data: InputData):
    dmatrix = xgb.DMatrix(np.array([data.features]))
    prediction = booster.predict(dmatrix)
    return {"prediction": int(prediction[0] >= 0.5)}  # 0 ou 1
