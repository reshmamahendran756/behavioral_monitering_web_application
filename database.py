from pymongo import MongoClient
from datetime import datetime, timezone
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client.behavioral_auth
sessions = db.sessions

def log_exam_session(user_id, confidence):
    sessions.insert_one({
        "user_id": user_id,
        "confidence": confidence,
        "status": "alert" if confidence < 60 else "continue",
        "time": datetime.now(timezone.utc)
    })

def get_sessions():
    return list(
        sessions.find({}, {"_id": 0}).sort("time", -1).limit(20)
    )
