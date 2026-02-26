## Instructions to use 


#### 1.Aim

 Aim - To make any make the footage enhanced by removing noise and enhancing the the footage through GAN models 


#### 2. Prerequisites

- Python(2.7 To 3.1) + scipy, numpy packages
- [TensorFlow (>=1.0.1)](https://www.tensorflow.org/install/) + [CUDA CuDNN](https://developer.nvidia.com/cudnn)
- Nvidia GPU(optional-For faster outputs)


#### 3. If you want to use this locally 

- Download the pre-trained [VGG-19 model](https://drive.google.com/drive/folders/1AQt-5a952dJH9kci-YMLkA3beApey6C8?usp=drive_link) and put it into `vgg_pretrained/` folder
<br/>


#### 5. Test the provided pre-trained models ( By default it takes input from the /input_images )

```bash
python test_model.py 
```

#### 6. To provide the custom location of input folder to the model 

```bash
python3 test_model.py "../human_detection/merged_results/<video_images>"
```

