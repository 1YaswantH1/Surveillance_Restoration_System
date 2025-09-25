import cv2
import os
from pathlib import Path

def images_to_video(input_folder, output_video_path, fps=30):
    """
    Convert a series of images in a folder to a video.
    
    Parameters:
    - input_folder: Path to the folder containing image frames.
    - output_video_path: Path where the output video will be saved (e.g., 'output.mp4').
    - fps: Frames per second for the output video (default is 30).
    """
    # Get list of image files from the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    # Sort files to ensure correct order
    image_files.sort()

    if not image_files:
        print("No images found in the specified folder.")
        return

    # Read the first image to get dimensions
    first_image_path = os.path.join(input_folder, image_files[0])
    first_image = cv2.imread(first_image_path)
    if first_image is None:
        print(f"Failed to load the first image: {first_image_path}")
        return
    height, width, _ = first_image.shape

    # Define the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    if not video_writer.isOpened():
        print("Error: Could not open video writer.")
        return

    # Process each image and add to video
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        frame = cv2.imread(image_path)
        
        if frame is None:
            print(f"Warning: Could not load image {image_path}. Skipping...")
            continue
        
        # Ensure frame dimensions match
        if frame.shape[:2] != (height, width):
            print(f"Warning: Image {image_file} has different dimensions. Resizing...")
            frame = cv2.resize(frame, (width, height))
        
        # Write frame to video
        video_writer.write(frame)
        print(f"Processed: {image_file}")

    # Release the video writer
    video_writer.release()
    print(f"Video saved successfully at: {output_video_path}")

def main():
    # Define input and output paths
    input_folder = "video-to-frame-images/test/1.test.mp4_images" # Replace with your folder path
    output_video_path = "frame-to-video/output/output_video.mp4"      # Replace with desired output path
    fps = 30                                    # Frames per second

    # Create output directory if it doesn't exist
    Path(output_video_path).parent.mkdir(parents=True, exist_ok=True)

    # Convert images to video
    images_to_video(input_folder, output_video_path, fps)

if __name__ == "__main__":
    main()