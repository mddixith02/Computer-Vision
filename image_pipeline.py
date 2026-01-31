from ultralytics import YOLO
import cv2
from blip_caption import generate_caption

model = YOLO("yolov8n.pt")

def detect_objects(image):
    results = model(image)[0]
    objects = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        objects.append(model.names[cls_id])

    return objects


def describe_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return "Image could not be loaded."

    # YOLO objects
    objects = detect_objects(image)
    unique_objects = set(objects)

    # BLIP caption
    blip_caption = generate_caption(image_path)

    if not unique_objects:
        return f"No objects detected. Caption: {blip_caption}"

    # Rule-based actions
    actions = []

    if "person" in unique_objects and "gun" in unique_objects:
        actions.append("holding a gun")

    if "person" in unique_objects and "phone" in unique_objects:
        actions.append("using a phone")

    # Environment detection
    environment = None
    if unique_objects & {"chair", "sofa", "tv", "vase"}:
        environment = "indoors"
    elif unique_objects & {"car", "road", "tree"}:
        environment = "outdoors"

    # Final description
    description = "The image contains " + ", ".join(unique_objects) + ". "

    if actions:
        description += "It shows a person " + " and ".join(actions) + ". "

    if environment:
        description += f"The scene appears to be {environment}. "

    description += "Overall, " + blip_caption + "."

    return description
