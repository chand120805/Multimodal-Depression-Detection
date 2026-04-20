import os
import numpy as np
import pickle

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from assessment.audio.pipeline import get_audio_features

DATASET_PATH = "dataset/audio"

X = []
y = []

print("🔄 Extracting features...")

for label in os.listdir(DATASET_PATH):

    label_path = os.path.join(DATASET_PATH, label)

    if not os.path.isdir(label_path):
        continue

    for file in os.listdir(label_path):

        file_path = os.path.join(label_path, file)

        try:
            features = get_audio_features(file_path)

            if features is not None:
                X.append(features)
                y.append(int(label))

        except Exception as e:
            print("❌ Error:", file_path)

X = np.array(X)
y = np.array(y)

print("✅ Total samples:", len(X))

# -----------------------------
# SCALE FEATURES
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# -----------------------------
# TRAIN MODEL
# -----------------------------
print("🤖 Training SVR model...")

model = SVR(kernel='rbf')
model.fit(X_train, y_train)

# -----------------------------
# EVALUATION
# -----------------------------
score = model.score(X_test, y_test)
print("📊 Model R² Score:", score)

# -----------------------------
# SAVE MODEL
# -----------------------------
os.makedirs("assessment/models", exist_ok=True)

with open("assessment/models/audio_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("assessment/models/audio_scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model + Scaler saved successfully!")