import parselmouth
from parselmouth.praat import call

def get_voice_quality(file_path):
    snd = parselmouth.Sound(file_path)

    # Create pitch
    pitch = call(snd, "To Pitch", 0.0, 75, 500)

    # Create point process (needed for jitter/shimmer)
    point_process = call(snd, "To PointProcess (periodic, cc)", 75, 500)

    # ✅ Jitter
    jitter = call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)

    # ✅ Shimmer
    shimmer = call(
        [snd, point_process],
        "Get shimmer (local)",
        0, 0, 0.0001, 0.02, 1.3, 1.6
    )

    return jitter, shimmer