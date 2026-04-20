import librosa

def load_audio(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    return y, sr

def trim_silence(y):
    yt, _ = librosa.effects.trim(y)
    return yt

def normalize_audio(y):
    return librosa.util.normalize(y)

def preprocess_audio(file_path):
    y, sr = load_audio(file_path)
    y = trim_silence(y)
    y = normalize_audio(y)
    return y, sr