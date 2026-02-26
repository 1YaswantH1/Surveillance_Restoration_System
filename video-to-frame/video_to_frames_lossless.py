import cv2
import os
from pathlib import Path
import argparse


def video_to_frames(video_path, output_folder=None):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    video_name = Path(video_path).stem

    if output_folder is None:
        output_folder = f"{video_name}_frames"

    os.makedirs(output_folder, exist_ok=True)

    print(f"FPS: {fps}")
    print(f"Total Frames: {total}")

    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(output_folder, f"frame_{frame_id:06d}.png")
        cv2.imwrite(frame_path, frame)
        frame_id += 1

    cap.release()

    with open(os.path.join(output_folder, "fps.txt"), "w") as f:
        f.write(str(fps))

    print("Frames saved in:", output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, required=True)
    args = parser.parse_args()

    video_to_frames(args.video_path)
