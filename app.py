import os, json
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from flask_cors import CORS
from flask_dance.contrib.google import make_google_blueprint
from dotenv import load_dotenv

from database import log_exam_session, get_sessions
from biometric_engine import predict_identity
from mlmodel import extract_features_enrollment, save_model

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

CORS(app, supports_credentials=True)

google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    redirect_to="enroll",
    scope=["openid", "email", "profile"]
)
app.register_blueprint(google_bp, url_prefix="/login")

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/enroll", methods=["GET", "POST"])
def enroll():
    if not google_bp.authorized:
        return redirect(url_for("google.login"))

    resp = google_bp.session.get("https://openidconnect.googleapis.com/v1/userinfo")
    user = resp.json()
    session["user_id"] = user["email"]

    if request.method == "POST":
        events = json.loads(request.form["keystroke_data"])
        features = extract_features_enrollment(events)

        if features is None:
            return jsonify({"error": "Not enough typing data"}), 400

        save_model(features)
        return jsonify({"status": "Enrollment successful"})

    return render_template("enroll.html")

@app.route("/exam", methods=["POST"])
def exam():
    if "user_id" not in session:
        return jsonify({"error": "unauthorized"}), 401

    events = request.json
    _, confidence = predict_identity(events)

    if confidence < 60:
        log_exam_session(session["user_id"], confidence)
        return jsonify({"action": "alert", "confidence": confidence})

    return jsonify({"action": "continue", "confidence": confidence})

@app.route("/admin")
def admin():
    if session.get("user_id") != os.getenv("ADMIN_EMAIL"):
        return "Access denied", 403
    return render_template("admin.html")

@app.route("/api/admin/sessions")
def admin_sessions():
    return jsonify(get_sessions())

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("google.login"))

if __name__ == "__main__":
    app.run(debug=True)
