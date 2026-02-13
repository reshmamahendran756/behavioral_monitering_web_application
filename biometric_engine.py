import joblib
import numpy as np

MODEL = joblib.load("models/model.pkl")
SCALER = joblib.load("models/scaler.pkl")
ENCODER = joblib.load("models/label_encoder.pkl")

def predict_identity(events):
    if len(events) < 15:
        return None, 0

    X = []
    for e in events:
        dwell = e.get("dwell", 0)
        flight = e.get("flight", 0)
        X.append([dwell, flight, 0, 0])

    X = np.array(X)
    Xs = SCALER.transform(X)

    probs = MODEL.predict_proba(Xs)
    avg = np.mean(probs, axis=0)

    idx = np.argmax(avg)
    user = ENCODER.inverse_transform([idx])[0]
    confidence = round(avg[idx] * 100, 2)

    return user, confidence
