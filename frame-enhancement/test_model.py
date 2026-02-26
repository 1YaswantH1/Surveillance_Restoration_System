import imageio.v2 as imageio
from PIL import Image
import numpy as np
import tensorflow as tf
from models import resnet
import utils
import os
import sys

tf.compat.v1.disable_v2_behavior()

# === CONFIGURATION ===
# Default settings (no need to pass via CLI)
phone = "iphone_orig"
dped_dir = "dped/"
resolution = "orig"
use_gpu = False
iteration = "all"
test_subset = "full"

# Image folders
# === INPUT / OUTPUT FOLDERS ===

# === INPUT / OUTPUT FOLDERS ===

base_output_root = "output"
os.makedirs(base_output_root, exist_ok=True)

if len(sys.argv) > 1:
    input_folder = sys.argv[1]

    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder '{input_folder}' does not exist.")

    folder_name = os.path.basename(os.path.normpath(input_folder))
    base_output = os.path.join(
        base_output_root, "custom_vedio", f"{folder_name}_enhanced"
    )

    output_folder = os.path.join(base_output, "enhanced")
    output_folder1 = os.path.join(base_output, "before_after")

else:
    input_folder = "input_images"
    output_folder = os.path.join(base_output_root, "output_images_1")
    output_folder1 = os.path.join(base_output_root, "output_images_2")

os.makedirs(output_folder, exist_ok=True)
os.makedirs(output_folder1, exist_ok=True)

# Get available resolutions and specified resolution
res_sizes = utils.get_resolutions()
IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_SIZE = utils.get_specified_res(
    res_sizes, phone, resolution
)

# Disable GPU if needed
config = tf.compat.v1.ConfigProto(device_count={"GPU": 0}) if not use_gpu else None

# Placeholders and model
x_ = tf.compat.v1.placeholder(tf.float32, [None, IMAGE_SIZE])
x_image = tf.reshape(x_, [-1, IMAGE_HEIGHT, IMAGE_WIDTH, 3])
enhanced = resnet(x_image)


def to_uint8(img):
    return np.clip(img * 255.0, 0, 255).astype(np.uint8)


with tf.compat.v1.Session(config=config) as sess:
    valid_ext = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")

    test_photos = [
        f
        for f in os.listdir(input_folder)
        if os.path.isfile(os.path.join(input_folder, f))
        and not f.startswith(".")
        and f.lower().endswith(valid_ext)
    ]
    if test_subset == "small":
        test_photos = test_photos[:5]

    if phone.endswith("_orig"):
        saver = tf.compat.v1.train.Saver()
        checkpoint_path = os.path.join("models_orig", phone)

        if not os.path.exists(checkpoint_path + ".index"):
            raise FileNotFoundError(
                f"No checkpoint files found for {phone} in models_orig/"
            )

        saver.restore(sess, checkpoint_path)

        for photo in test_photos:
            print("Processing image:", photo)

            raw_image = imageio.imread(os.path.join(input_folder, photo))
            resized_image = Image.fromarray(raw_image).resize(
                (res_sizes[phone][1], res_sizes[phone][0])
            )
            image = np.asarray(resized_image).astype(np.float32) / 255.0

            image_crop = utils.extract_crop(image, resolution, phone, res_sizes)
            image_crop_2d = np.reshape(image_crop, [1, IMAGE_SIZE])

            enhanced_2d = sess.run(enhanced, feed_dict={x_: image_crop_2d})
            enhanced_image = np.reshape(enhanced_2d, [IMAGE_HEIGHT, IMAGE_WIDTH, 3])

            before_after = np.hstack((image_crop, enhanced_image))
            photo_name = os.path.splitext(photo)[0]

            imageio.imwrite(
                os.path.join(output_folder, f"{photo_name}_enhanced.png"),
                to_uint8(enhanced_image),
            )
            imageio.imwrite(
                os.path.join(output_folder1, f"{photo_name}_before_after.png"),
                to_uint8(before_after),
            )

    else:
        num_saved_models = int(
            len(
                [f for f in os.listdir("models/") if f.startswith(phone + "_iteration")]
            )
            / 2
        )
        iterations = (
            np.arange(1, num_saved_models) * 1000
            if iteration == "all"
            else [int(iteration)]
        )

        for i in iterations:
            saver = tf.compat.v1.train.Saver()
            saver.restore(sess, f"models/{phone}_iteration_{i}.ckpt")

            for photo in test_photos:
                print(f"Iteration {i}, processing image {photo}")

                raw_image = imageio.imread(os.path.join(input_folder, photo))
                resized_image = Image.fromarray(raw_image).resize(
                    (res_sizes[phone][1], res_sizes[phone][0])
                )
                image = np.asarray(resized_image).astype(np.float32) / 255.0

                image_crop = utils.extract_crop(image, resolution, phone, res_sizes)
                image_crop_2d = np.reshape(image_crop, [1, IMAGE_SIZE])

                enhanced_2d = sess.run(enhanced, feed_dict={x_: image_crop_2d})
                enhanced_image = np.reshape(enhanced_2d, [IMAGE_HEIGHT, IMAGE_WIDTH, 3])

                before_after = np.hstack((image_crop, enhanced_image))
                photo_name = os.path.splitext(photo)[0]

                imageio.imwrite(
                    os.path.join(
                        output_folder, f"{photo_name}_iteration_{i}_enhanced.png"
                    ),
                    to_uint8(enhanced_image),
                )
                imageio.imwrite(
                    os.path.join(
                        output_folder, f"{photo_name}_iteration_{i}_before_after.png"
                    ),
                    to_uint8(before_after),
                )
