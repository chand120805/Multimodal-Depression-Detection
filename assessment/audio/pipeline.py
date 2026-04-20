import numpy as np
from .preprocess import preprocess_audio
from .features import extract_features
from .voice_quality import get_voice_quality

def get_audio_features(file_path):
    y, sr = preprocess_audio(file_path)

    if len(y) == 0:
        return None

    base_features = extract_features(y, sr)
    jitter, shimmer = get_voice_quality(file_path)

    final_features = np.hstack([base_features, jitter, shimmer])

    return final_features