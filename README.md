# 🧠 Multimodal Depression Detection System

A **Django-based AI system** that predicts depression severity using a combination of:

* 📋 PHQ-8 Questionnaire (clinical scoring)
* 📝 Text Analysis (NLP-based emotional understanding)
* 🎧 Audio Analysis (speech signal processing + ML)

---

# 🚀 Project Overview

This project implements a **multimodal approach** to mental health assessment by combining:

| Modality | Description                                 |
| -------- | ------------------------------------------- |
| PHQ-8    | Standard clinical questionnaire             |
| Text     | User-written responses analyzed using NLP   |
| Audio    | Voice signals analyzed using ML (SVR model) |

👉 Final output = **Combined Depression Score + Suggestions**

---

# 🧠 Key Features

* ✅ Multimodal AI system (Text + Audio + Questionnaire)
* ✅ Real-time audio processing
* ✅ Machine Learning model (SVR)
* ✅ Feature extraction using Librosa & Parselmouth
* ✅ Interactive dashboard with results
* ✅ Personalized suggestions based on score
* ✅ Clean Django-based UI

---

# 🧩 System Architecture

```
User Input
   ↓
--------------------------------
| PHQ Score | Text | Audio |
--------------------------------
   ↓
Feature Extraction
   ↓
ML Models (SVR + NLP)
   ↓
Score Fusion
   ↓
Final Depression Level
```

---

# 🎧 Audio Processing Pipeline

```
Audio (.wav)
   ↓
Feature Extraction:
   - MFCC
   - Pitch
   - Energy
   - Jitter
   - Shimmer
   ↓
StandardScaler
   ↓
SVR Model
   ↓
Predicted Score
```

---

# 🤖 Machine Learning Model

* Model: **Support Vector Regression (SVR)**
* Dataset: **RAVDESS**
* Target: Emotion → mapped to depression severity
* Evaluation: R² Score

---

# ⚙️ Installation Guide (Step-by-Step)

## 🔹 1. Clone Repository

```
git clone https://github.com/chand120805/Multimodal-Depression-Detection.git
cd Multimodal-Depression-Detection
```

---

## 🔹 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

## 🔹 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔹 4. Install Audio Dependencies

Some libraries require additional setup:

### ▶ Install FFmpeg (required for audio processing)

Download:
https://ffmpeg.org/download.html

Add to PATH.

---

## 🔹 5. Run Migrations

```
python manage.py migrate
```

---

## 🔹 6. Run Server

```
python manage.py runserver
```

---

## 🔹 7. Open in Browser

```
http://127.0.0.1:8000
```

---

# 📊 Dataset Information

* Dataset used: **RAVDESS**
* Contains emotional speech recordings
* Used for training audio model

⚠️ Dataset is not included due to size constraints

👉 Download from:
[kaggle](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

---

# 🏋️‍♂️ Training the Audio Model

To retrain model:

```
python train_audio_model.py
```

This will:

* Extract features
* Train SVR model
* Save:

  * audio_model.pkl
  * audio_scaler.pkl

---

# 📈 Output Example

```
Score: 12.64 / 32
Level: Mild 🙂

Breakdown:
- PHQ Score: X
- Text Score: Y
- Audio Score: Z
```

---



# ⚠️ Disclaimer

This system is:

❌ NOT a medical diagnosis tool
✔ ONLY for awareness and educational purposes

Always consult a professional for mental health concerns.

---

# 🛠 Tech Stack

* Python
* Django
* Scikit-learn
* Librosa
* Parselmouth
* HTML / CSS / JS

---

# 🚀 Future Improvements

* 🔹 Deep Learning models (LSTM, CNN)
* 🔹 Real clinical datasets
* 🔹 Real-time voice recording
* 🔹 Mobile app integration
* 🔹 Better multimodal fusion

---

# 👩‍💻 Author

**Sree Sai Chandana Kunta**

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!
