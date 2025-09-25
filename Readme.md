# Smart Surveillance Restoration System

## Abstract -

Surveillance videos are critical for forensic investigations but often suffer from quality issues such as blur, low lighting, damaged frames, and background noise, rendering them unreliable. Our solution take the Vedio as input split the vedio based on the motion that is send to the Model which trained Scale invarient feature extraction(same photo of object from diffrent devices may not show the same image they show different view of same object so model trained on same patch to reduce the parameter and beter generalisation) to enhance the vedio.

## Instruction to use (Setup)-

```bash
cd frame-to-video
```

```bash
pip install -r requirements.txt
```

```bash
cd video-to-frame
```

```bash
pip install -r requirements.txt
```

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

```bash
cd frame-enhancement
```

Download the pre-trained [VGG-19 model](https://drive.google.com/drive/folders/1AQt-5a952dJH9kci-YMLkA3beApey6C8?usp=drive_link) and put it into `vgg_pretrained/` folder