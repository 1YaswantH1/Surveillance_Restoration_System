import os
import subprocess
import glob

# Get absolute root directory (very important)
ROOT_DIR = os.getcwd()

# ==============================
# STEP 1: RECORD VIDEO
# ==============================
try:
    os.chdir(os.path.join(ROOT_DIR, "human_detection"))
    print("Recording... Press Ctrl+C to stop.")
    subprocess.run(["python3", "camera_recorder.py"])
except KeyboardInterrupt:
    print("\nRecording stopped. Continuing pipeline...")

# ==============================
# STEP 2: GET LATEST RECORDED VIDEO
# ==============================
records_path = os.path.join("records")
video_files = glob.glob(os.path.join(records_path, "*.mp4"))

if not video_files:
    raise Exception("No recorded videos found.")

latest_video = max(video_files, key=os.path.getctime)
print(f"Latest recorded video: {latest_video}")

# ==============================
# STEP 3: RUN HUMAN DETECTION
# ==============================
subprocess.run(["python3", "human_detection.py", latest_video])

# ==============================
# STEP 4: MERGE CLIPS
# ==============================
subprocess.run(["python3", "merge_footage.py"])

# ==============================
# STEP 5: GET LATEST MERGED VIDEO
# ==============================
merged_path = os.path.join("merged_results")
merged_videos = glob.glob(os.path.join(merged_path, "*_merged.mp4"))

if not merged_videos:
    raise Exception("No merged videos found.")

latest_merged = max(merged_videos, key=os.path.getctime)
print(f"Merged video: {latest_merged}")

# Go back to root
os.chdir(ROOT_DIR)

# ==============================
# STEP 6: CONVERT MERGED VIDEO TO FRAMES
# ==============================
os.chdir(os.path.join(ROOT_DIR, "video-to-frame"))

subprocess.run([
    "python3",
    "video_to_frames.py",
    "--video_path",
    os.path.join(ROOT_DIR, "human_detection", latest_merged),
])

# Return to root
os.chdir(ROOT_DIR)

# ==============================
# STEP 7: FIND FRAME IMAGES FOLDER
# ==============================
frames_base_path = os.path.join(ROOT_DIR, "human_detection", "merged_results")

image_folders = [
    os.path.join(frames_base_path, f)
    for f in os.listdir(frames_base_path)
    if f.endswith("_images")
]

if not image_folders:
    raise Exception("No frame image folders found.")

latest_frames_folder = max(image_folders, key=os.path.getctime)
print(f"Frames folder detected: {latest_frames_folder}")

# ==============================
# STEP 8: RUN IMAGE ENHANCEMENT
# ==============================
os.chdir(os.path.join(ROOT_DIR, "frame-enhancement"))

subprocess.run([
    "python3",
    "test_model.py",
    latest_frames_folder
])

print("\n🚀 FULL PIPELINE COMPLETED SUCCESSFULLY 🚀")
