from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model(
    "videos/sample.mp4",
    save=True,
    show=True
)

print("Video detection completed successfully!")