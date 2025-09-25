import cv2
import os
import sys
from math import ceil
import argparse


def save_frames_for_file(full_video_path, video_file, max_frames, skip_first, rotate):
    print(video_file)

    folder_for_video_save = f'{full_video_path}_images'
    os.makedirs(folder_for_video_save, exist_ok=True)

    cap = cv2.VideoCapture(full_video_path)
    print(f'Parsing file: {full_video_path}')

    fps = cap.get(cv2.CAP_PROP_FPS)
    frames_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    durationInSeconds = float(frames_num) / float(fps)

    write_num = ceil((frames_num - (fps * skip_first)) / max_frames)

    print(f'fps: {fps} | frames: {frames_num} | write_num: {write_num}')

    counter = 1

    for i in range(int(frames_num - 1)):
        if i < skip_first:
            cap.grab()
            continue
        ret, frame = cap.read()
        if not ret:
            print(i)
            break
        if rotate is not None:
            if rotate == 0:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            else:
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        h, w, _ = frame.shape
        # frame = = frame[int(h*0.1):h, int(w*0.1):w]
        # frame = frame[0:h, int(w*0.1):w]
        # frame = frame[0:int(h*0.9), 0:w]
        if counter == write_num:
            image_name = f'{folder_for_video_save}/{video_file}_{i}.jpg'
            cv2.imwrite(image_name, frame)
            # print(f'image saved: {image_name}')
            counter = 0
        counter += 1


def video_to_frames(video_path, max_frames=200, skip_first=5, rotate=None):
    """
        max_frames : target frame number from the video
        skip_first : skip first k frames at the begining of the video
        rotate : None - no rotation, 0 - clockwise, 1 - counterclockwise
    """
    full_video_path = video_path

    if os.path.isdir(video_path):
        print("\nParsing video directory")

        videos = os.listdir(video_path)
        for video_file in videos:
            full_video_path = f'{video_path}/{video_file}'
            if not os.path.isdir(full_video_path):
                #print(f'NOT DIR: {full_video_path} | path: {video_path} | file: {video_file}')

                save_frames_for_file(full_video_path, video_file, max_frames, skip_first, rotate)
    elif os.path.isfile(video_path):
        print("\nParsing video file")
        video_path = video_path.split('/')
        video_path = video_path[len(video_path) - 1]

        save_frames_for_file(full_video_path, video_path, max_frames, skip_first, rotate)
    else:
        print("You send broken file path")
        return



if __name__ == '__main__':
    ### parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, help='path to video', default='')
    # какой по счёту кадр брать. Если поставить 5, то будет брать каждый пятый кадр
    parser.add_argument('--skip_first', type=int, help='how much frames to skip', default=0)
    parser.add_argument('--rotate', type=int,
                        help='rotate : None - no rotation, 0 - clockwise, 1 - counterclockwise',
                        default=None)

    args = parser.parse_args()

    # skip_first=args.skip_first
    video_to_frames(args.video_path, max_frames=200, skip_first=args.skip_first, rotate=args.rotate)
    # video_to_frames(args.video_path, args.folder_to_save, max_frames = 200, skip_first=5,rotate=None)
