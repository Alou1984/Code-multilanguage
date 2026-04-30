# model.py
import numpy as np

def predict_force(mass, distance):
    # Fake "antigravity" AI approximation
    return mass / (distance**2 + 1e-5)