import cv2
import os
from pathlib import Path

def images_to_video(input_folder, output_video_path, fps=30):
    """
    Convert a series of images in a folder to a video.
    
    Parameters:
    - input_folder: Path to the folder containing image frames.
    - output_video_path: Path where the output video will be saved (e.g., 'output_videos/my_video.mp4').
    - fps: Frames per second for the output video (default is 30).
    """
    # Get list of image files from the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    # Sort files to ensure correct order
    image_files.sort()

    if not image_files:
        print("No images found in the specified folder.")
        return False

    # Read the first image to get dimensions
    first_image_path = os.path.join(input_folder, image_files[0])
    first_image = cv2.imread(first_image_path)
    if first_image is None:
        print(f"Failed to load the first image: {first_image_path}")
        return False
    height, width, _ = first_image.shape

    # Define the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    if not video_writer.isOpened():
        print("Error: Could not open video writer.")
        return False

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
    return True

def main():
    # Fixed output folder
    output_folder = "frame-to-video/output"  # Fixed output folder in the current directory

    # Prompt for input folder
    while True:
        input_folder = input("Enter the path to the folder containing image frames: ").strip()
        if os.path.isdir(input_folder):
            break
        print(f"Error: '{input_folder}' does not exist or is not a directory. Please try again.")

    # Prompt for output video file name
    while True:
        output_video_name = input("Enter the output video file name (e.g., my_video.mp4): ").strip()
        if output_video_name:
            # Ensure the file has a valid extension
            if not output_video_name.endswith(('.mp4', '.avi')):
                output_video_name += '.mp4'  # Default to .mp4 if no valid extension
            break
        print("Error: Output video file name cannot be empty. Please try again.")

    # Combine fixed output folder with video file name
    output_video_path = os.path.join(output_folder, output_video_name)

    # Prompt for FPS with default
    while True:
        fps_input = input("Enter frames per second (FPS) for the video [default is 30]: ").strip()
        if not fps_input:
            fps = 30
            break
        try:
            fps = int(fps_input)
            if fps > 0:
                break
            print("Error: FPS must be a positive number. Please try again.")
        except ValueError:
            print("Error: FPS must be a valid number. Please try again.")

    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Convert images to video
    success = images_to_video(input_folder, output_video_path, fps)
    if not success:
        print("Failed to create video.")

if __name__ == "__main__":
    main()