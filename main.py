from image_pipeline import describe_image
from video_pipeline import describe_video
import os

IMAGE_DIR = "input/Image"
VIDEO_DIR = "input/Video"

print("Choose input type:")
print("1. Image")
print("2. Video")

choice = input("Enter choice: ").strip()

if choice == "1":
    image_name = input("Enter image name (e.g. test.jpg): ").strip()
    path = os.path.join(IMAGE_DIR, image_name)

    if not os.path.isfile(path):
        print("Image not found in inputs/images/")
    else:
        print(describe_image(path))

elif choice == "2":
    video_name = input("Enter video name (e.g. test.mp4): ").strip()
    path = os.path.join(VIDEO_DIR, video_name)

    if not os.path.isfile(path):
        print("Video not found in inputs/videos/")
    else:
        print(describe_video(path))

else:
    print("Invalid choice")
