import cv2
import os
from blip_caption import generate_caption

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_frames(video_path, interval=30):
    cap = cv2.VideoCapture(video_path)
    frames = []

    frame_id = 0
    saved_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % interval == 0:
            frame_path = os.path.join(OUTPUT_DIR, f"frame_{saved_id}.jpg")
            cv2.imwrite(frame_path, frame)
            frames.append(frame_path)
            saved_id += 1

        frame_id += 1

    cap.release()
    return frames


def describe_video(video_path):
    frames = extract_frames(video_path)

    if not frames:
        return "Unable to extract frames from the video."

    captions = []

    for frame_path in frames:
        caption = generate_caption(frame_path)
        captions.append(caption)

    # Remove duplicates while preserving order
    unique_captions = list(dict.fromkeys(captions))

    # Limit output size
    summary_captions = unique_captions[:3]

    description = "The video appears to show "

    description += "; ".join(summary_captions) + "."

    return description
