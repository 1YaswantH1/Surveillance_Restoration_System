# Smart Surveillance Restoration System

## Surveillance Restoration Results
<table>
<tr>
<td align="center">

<b>Before Enhancement</b><br>
<a href="[https://youtu.be/a-a-rn-Ys3c](https://youtu.be/u9-9QtOIgAE?si=ga0K9s6PPQOoybmu)">
</a>

</td>
<td align="center">

<b>After Enhancement</b><br>
<a href="[https://youtu.be/qb4xUp7SAjk](https://www.youtube.com/watch?v=8r38UFpw-aA)">

</a>

</td>
</tr>
</table> 

## Aim - Enhances the vedio footage quality,changes black and white footage to color footage

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
