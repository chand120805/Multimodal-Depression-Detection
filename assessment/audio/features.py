import numpy as np
import librosa

def extract_features(y, sr):
    features = []

    # MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    features.extend(np.mean(mfcc, axis=1))
    features.extend(np.std(mfcc, axis=1))

    # Chroma
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    features.extend(np.mean(chroma, axis=1))

    # Mel Spectrogram
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    features.append(np.mean(mel))

    # Spectral
    features.append(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    features.append(np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr)))
    features.append(np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr)))

    # Energy
    features.append(np.mean(librosa.feature.rms(y=y)))

    # ZCR
    features.append(np.mean(librosa.feature.zero_crossing_rate(y)))

    # Pitch
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch = pitches[pitches > 0]
    features.append(np.mean(pitch) if len(pitch) > 0 else 0)

    return np.array(features)