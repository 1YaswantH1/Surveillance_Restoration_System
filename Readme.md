# Smart Surveillance Restoration System

## Surveillance Restoration Results
<table>
<tr>
<td align="center">

<b>Before Enhancement</b><br>
<a href="https://youtu.be/a-a-rn-Ys3c">
  <img src="Results/Before%20Enhancing%20Thumbnail.png" width="400">
</a>

</td>
<td align="center">

<b>After Enhancement</b><br>
<a href="https://youtu.be/qb4xUp7SAjk">
  <img src="Results/After%20Enhancing%20thumbnail.png" width="400">
</a>

</td>
</tr>
</table> 

## Abstract -

The surveillance video footage serves as vital evidence for forensic investigations yet it becomes unreliable because of various problems which include blurry images and insufficient illumination and visual interference and corrupted video segments.

Our solution accepts surveillance video content as its starting point before it performs motion-based segmentation to create multiple video segments. The trained enhancement model receives these segments to perform its operations through scale-invariant feature extraction. The model learns to identify identical objects which show up differently between various devices and camera setups. The model learns from stable object patches which leads it to reduce redundant parameters while it develops better generalization abilities that produce superior enhanced footage for investigative work.

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
