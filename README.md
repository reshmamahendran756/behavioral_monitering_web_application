# behavioral_monitering_web_application

📌 Project Overview
This project implements a Behavioral Biometric Authentication System that continuously verifies a student's identity during an online examination using keystroke dynamics.
Instead of relying only on login credentials, the system analyzes how a user types — measuring dwell time, flight time, typing speed, and error behavior — to generate a unique behavioral fingerprint.
If suspicious typing behavior is detected during an exam, the system triggers alerts to prevent impersonation.

🎯 Problem Statement
Online examinations are vulnerable to:
Identity impersonation
Proxy test-taking
Unauthorized user substitution
Credential sharing
Traditional authentication methods (password, OTP, login) verify identity only at the start of the session.
This project solves that limitation by enabling continuous authentication using typing behavior.

🚀 Key Features
1️⃣ Behavioral Enrollment
Captures keystroke dynamics during registration
Extracts statistical features:
Mean dwell time
Standard deviation of dwell
Mean flight time
Standard deviation of flight
Typing speed
Backspace frequency
Stores a biometric typing profile

2️⃣ Real-Time Exam Monitoring
Continuously collects typing data during exam
Compares live behavior with enrolled profile
Uses cosine similarity for identity confidence scoring
Generates confidence score in percentage

3️⃣ Intelligent Alert Mechanism
If confidence drops below threshold:
Suspicious typing detected
Admin is alerted
Logs exam session activity to database

4️⃣ Admin Dashboard
View last 20 exam sessions
Monitor:
User ID
Confidence score
Status (Alert / Continue)
Enables monitoring of potential impersonation

🧮 Technical Approach
🔍 Feature Engineering

Extracted behavioral metrics:
Keystroke dwell time
Inter-key flight time
Typing speed
Error frequency (backspace usage)

📊 Similarity Model
Instead of a heavy ML classifier, the system uses:
Feature normalization
Cosine similarity comparison
Threshold-based anomaly detection

This makes the system:
Lightweight
Interpretable
Real-time capable
Easily deployable

🛠️ Tech Stack
Layer	Technology
Backend	Flask
Frontend	HTML, JavaScript
Authentication	Google OAuth
Database	MongoDB
ML / Analytics	NumPy, Scikit-learn
Hosting Ready	Any WSGI server

🏗️ System Workflow
User logs in via Google OAuth
User completes typing-based enrollment
Biometric profile is generated and stored
During exam:
Keystrokes captured every 10 seconds
Features extracted
Similarity computed
Confidence returned
Admin can monitor suspicious activity

📈 Applications
Online university examinations
Certification platforms
Remote proctoring systems
E-learning authentication
Corporate compliance testing

🔐 Why Behavioral Biometrics?

Unlike passwords:
Cannot be easily shared
Hard to mimic consistently
Passive and non-intrusive
Works continuously in background

📊 Advantages
Continuous authentication
Lightweight ML model
Real-time anomaly detection
Minimal hardware requirements

Privacy-preserving (no camera required)
⚡ Future Improvements
Multi-sample enrollment
Adaptive threshold tuning
Mouse dynamics integration
Deep learning-based anomaly detection
Cloud deployment with scaling
ROC-based evaluation metrics

📚 Academic Value

This project demonstrates:
Behavioral biometrics
Feature engineering
Real-time anomaly detection
Continuous authentication systems
Applied machine learning in cybersecurity

💡 Innovation Highlight

This system moves from static authentication to continuous behavioral identity verification, significantly improving the security of online examination platforms.
