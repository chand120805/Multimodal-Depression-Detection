import numpy as np
import librosa
import tempfile
import os
from pydub import AudioSegment

from .features import extract_features
from .voice_quality import get_voice_quality


def get_audio_features(audio_input):
    try:
        # ----------------------------------------
        # CASE 1: FILE PATH (TRAINING)
        # ----------------------------------------
        if isinstance(audio_input, str):
            y, sr = librosa.load(audio_input, sr=None)
            temp_path = audio_input

        # ----------------------------------------
        # CASE 2: AUDIO STREAM (WEB APP)
        # ----------------------------------------
        else:
            # 🔥 Step 1: Save raw uploaded file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".input") as raw_tmp:
                raw_path = raw_tmp.name
                audio_input.seek(0)
                raw_tmp.write(audio_input.read())

            # 🔥 Step 2: Convert to WAV using ffmpeg (via pydub)
            audio = AudioSegment.from_file(raw_path)
            audio = audio.set_frame_rate(16000).set_channels(1)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as wav_tmp:
                temp_path = wav_tmp.name

            audio.export(temp_path, format="wav")

            # 🔥 Step 3: Load WAV (safe)
            y, sr = librosa.load(temp_path, sr=None)

            # cleanup raw file
            os.remove(raw_path)

        # ----------------------------------------
        # EMPTY AUDIO CHECK
        # ----------------------------------------
        if y is None or len(y) == 0:
            return None

        # ----------------------------------------
        # FEATURE EXTRACTION
        # ----------------------------------------
        base_features = extract_features(y, sr)

        jitter, shimmer = get_voice_quality(temp_path)

        final_features = np.hstack([base_features, jitter, shimmer])

        # cleanup wav temp (only for stream)
        if not isinstance(audio_input, str) and os.path.exists(temp_path):
            os.remove(temp_path)

        return final_features

    except Exception as e:
        print("Audio error:", e)
        return None