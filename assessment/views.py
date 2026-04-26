from django.shortcuts import render
from .models import Assessment
from django.contrib.auth.decorators import login_required
from .nlp_model import get_text_score
from .ai_suggestions import generate_ai_suggestions
from .audio.pipeline import get_audio_features

import numpy as np
import os
from django.conf import settings
import uuid

import pickle

from cryptography.fernet import Fernet
import io
fernet = Fernet(settings.ENCRYPTION_KEY.encode())

# Load once (global)
with open("assessment/models/audio_model.pkl", "rb") as f:
    audio_model = pickle.load(f)

with open("assessment/models/audio_scaler.pkl", "rb") as f:
    audio_scaler = pickle.load(f)
    
# -------------------------------
# SAVE AUDIO FILE
# -------------------------------
def save_encrypted_audio(file):
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    filename = f"{uuid.uuid4()}_{file.name}.enc"
    path = os.path.join(settings.MEDIA_ROOT, filename)

    # read raw file
    raw_data = file.read()

    # encrypt
    encrypted_data = fernet.encrypt(raw_data)

    # save encrypted file
    with open(path, 'wb') as f:
        f.write(encrypted_data)

    return path

def load_audio(path):
    with open(path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

def delete_audio(path):
    if os.path.exists(path):
        os.remove(path)


# -------------------------------
# PHQ QUESTIONS
# -------------------------------
PHQ_QUESTIONS = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, irritable or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself – or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as school work, reading or watching television",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite – being so fidgety or restless that you have been moving around a lot more than usual"
]


# -------------------------------
# SEVERITY
# -------------------------------
def calculate_severity(score):
    if score <= 4:
        return "Minimal"
    elif score <= 9:
        return "Mild"
    elif score <= 14:
        return "Moderate"
    elif score <= 19:
        return "Moderately Severe"
    else:
        return "Severe"


# -------------------------------
# MAIN VIEW
# -------------------------------
@login_required
def questionnaire(request):
    if request.method == 'POST':

        # PHQ scores
        q = [int(request.POST.get(f'q{i}')) for i in range(1, 9)]

        # Text answers
        t = [request.POST.get(f't{i}', '') for i in range(1, 9)]

        # -------------------------------
        # PHQ SCORE
        # -------------------------------
        phq_score = sum(q)

        # -------------------------------
        # NLP SCORE
        # -------------------------------
        valid_texts = [text for text in t if text.strip() != ""]

        if valid_texts:
            nlp_scores = [get_text_score(text) for text in valid_texts]
            nlp_scaled = max(0, min(4, (sum(nlp_scores) / len(nlp_scores)) * 4))
        else:
            nlp_scaled = 0

        # -------------------------------
        # AUDIO SCORE
        # -------------------------------
        audio_file = request.FILES.get('audio')

        if audio_file:
            audio_path = save_encrypted_audio(audio_file)

            # decrypt temporarily
            audio_bytes = load_audio(audio_path)

            # convert to stream for librosa
            audio_stream = io.BytesIO(audio_bytes)

            # extract features
            audio_features = get_audio_features(audio_stream)
            print("Audio features:", audio_features)

            # 🔥 DELETE AFTER USE
            delete_audio(audio_path)

            if audio_features is not None:
                audio_features = audio_scaler.transform([audio_features])
                audio_score = audio_model.predict(audio_features)[0]
                # scale to 0–4
                audio_scaled = max(0, min(4, float(audio_score)))
            else:
                audio_scaled = 0
        else:
            audio_scaled = 0

        # -------------------------------
        # FINAL SCORE
        # -------------------------------
        final_score = phq_score + nlp_scaled + audio_scaled

        severity = calculate_severity(phq_score)
        suggestions = generate_ai_suggestions(q, t)

        # Save
        Assessment.objects.create(
            user=request.user,
            q1=q[0], q2=q[1], q3=q[2], q4=q[3],
            q5=q[4], q6=q[5], q7=q[6], q8=q[7],
            text1=t[0], text2=t[1], text3=t[2], text4=t[3],
            text5=t[4], text6=t[5], text7=t[6], text8=t[7],
            total_score=round(final_score, 2)
        )

        phq_max = 24
        text_max = 4
        audio_max = 4

        context = {
            'score': round(final_score, 2),
            'severity': severity,
            'suggestions': suggestions,
            'max_score': phq_max + text_max + audio_max,

            # breakdown
            'phq_score': phq_score,
            'phq_max': phq_max,

            'text_score': round(nlp_scaled, 2),
            'text_max': text_max,

            'audio_score': round(audio_scaled, 2),
            'audio_max': audio_max,
        }
        return render(request, 'result.html', context)
    return render(request, 'questionnaire.html', {
        'questions': PHQ_QUESTIONS
    })
