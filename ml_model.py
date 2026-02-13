import numpy as np
import pickle
import os
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

MODEL_FILE = "model.pkl"

def extract_features_enrollment(events):
    if len(events) < 30:
        return None

    dwell = [e["dwell"] for e in events if e["dwell"] > 0]
    flight = [e["flight"] for e in events if e["flight"] > 0]

    if len(dwell) < 10 or len(flight) < 10:
        return None

    time_span = (events[-1]["time"] - events[0]["time"]) / 1000
    speed = len(events) / time_span if time_span > 0 else 0
    backspaces = sum(1 for e in events if e["key"] == "Backspace")

    return np.array([
        np.mean(dwell),
        np.std(dwell),
        np.mean(flight),
        np.std(flight),
        speed,
        backspaces
    ])

def save_model(features):
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(features, f)

def load_model():
    if not os.path.exists(MODEL_FILE):
        return None
    with open(MODEL_FILE, "rb") as f:
        return pickle.load(f)

def predict_similarity(live, stored):
    X = np.vstack([stored, live])
    X = StandardScaler().fit_transform(X)
    return round(cosine_similarity([X[0]], [X[1]])[0][0] * 100, 2)
