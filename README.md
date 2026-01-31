Visual Description System (Image & Video)

* A Python-based computer vision project that generates natural language descriptions for images and videos by combining object detection (YOLOv8) and image captioning (BLIP).

This project focuses on understanding visual content, not just detecting objects.



Features

* Image description using YOLOv8 + BLIP

* Video description via frame sampling

* Action inference (e.g., person holding a gun)

* Scene context detection (indoors / outdoors)

* Modular, extensible pipeline design



How It Works

Images:-

* Detect objects using YOLOv8

* Generate captions using BLIP

* Combine objects + captions into a final description

Videos:-

* Sample frames at fixed intervals

* Run detection + captioning per frame

* Aggregate results for a stable video-level description



