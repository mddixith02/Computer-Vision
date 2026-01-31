from ultralytics import YOLO

# Load lightweight YOLO model
model = YOLO("yolov8n.pt")

def detect_objects(image):
    results = model(image, verbose=False)
    
    detected = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            detected.append(label)
    
    return detected
