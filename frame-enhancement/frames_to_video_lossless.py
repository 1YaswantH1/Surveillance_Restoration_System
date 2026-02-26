import cv2
import os
from pathlib import Path


def frames_to_video(input_folder, output_video_path):
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".png")])

    if not image_files:
        print("No frames found.")
        return

    # Read FPS from metadata
    fps_file = os.path.join(input_folder, "fps.txt")
    if os.path.exists(fps_file):
        with open(fps_file, "r") as f:
            fps = float(f.read())
    else:
        fps = 30  # fallback

    first_frame = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width = first_frame.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for file in image_files:
        frame = cv2.imread(os.path.join(input_folder, file))
        writer.write(frame)

    writer.release()
    print("Video reconstructed successfully.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_folder", type=str, required=True)
    parser.add_argument("--output_video", type=str, required=True)

    args = parser.parse_args()

    frames_to_video(args.input_folder, args.output_video)
