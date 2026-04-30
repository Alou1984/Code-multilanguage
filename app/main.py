# main.py
from fastapi import FastAPI
from model import predict_force

app = FastAPI()

@app.get("/predict")
def predict(mass: float, distance: float):
    result = predict_force(mass, distance)
    return {"force": result}