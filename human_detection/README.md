# Camera Recorder Application with Human Detection

This Python application allows you to record video from your computer's camera and save it as an MP4 file. It utilizes OpenCV library and YOLO (You Only Look Once) object detection algorithm for human detection.

## Requirements

- Python 3.x
- OpenCV library (`pip install opencv-python`)
- Pre-trained YOLO model: yolov3.cfg and yolov3.weights (`https://pjreddie.com/darknet/yolo/`)
- VLC media player (or any other compatible media player) to play the recorded videos
- ffmpeg (command-line tool) for video extraction (`https://ffmpeg.org/download.html`)

## Installation

1. Change direcory to human_detection
2. 
```bash
cd human_detection 
```

1. Download the pre-trained YOLO model:
   - Create a folder named "yolo" in the same directory as the Python script.
   - Download the YOLO configuration file (`yolov3.cfg`), pre-trained weights file (`yolov3.weights`)
   - Place these files in the "yolo" folder.

2. Install the required Python packages:
   
   ```
   pip install opencv-python numpy
   ```

3. Ensure you have VLC media player (or another compatible media player) installed on your system to play the recorded videos.

4. Optional:- Install ffmpeg (command-line tool) from the official website: `https://ffmpeg.org/download.html`. Make sure ffmpeg is accessible from the command line for video extraction .

## Usage

### To generate synthetic vedio for testing using camera

```bash
python -u "/pathto/camera_recorder.py
```

### To Run the Human detection code 

```bash
python -u "/pathto/human_detection.py"
```
