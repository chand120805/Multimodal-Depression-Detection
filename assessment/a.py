import os
import shutil

SOURCE = "C:\\Users\\kunta\\Downloads\\ravdess"          # your downloaded folder
DEST = "dataset/audio/"
# Create folders
for i in range(4):
    os.makedirs(os.path.join(DEST, str(i)), exist_ok=True)

# Walk through all subfolders 🔥
for root, dirs, files in os.walk(SOURCE):

    for file in files:

        if not file.endswith(".wav"):
            continue

        parts = file.split("-")
        emotion = int(parts[2])  # extract emotion

        # Mapping
        if emotion in [1, 3]:
            label = 0
        elif emotion in [2, 8]:
            label = 1
        elif emotion in [4, 7]:
            label = 2
        else:
            label = 3

        src_path = os.path.join(root, file)
        dest_path = os.path.join(DEST, str(label), file)

        shutil.copy(src_path, dest_path)

print("✅ Dataset organized successfully!")