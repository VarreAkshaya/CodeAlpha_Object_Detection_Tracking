from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model(
    "sample.jpg",
    save=True,
    conf=0.5
)

print("Detection completed successfully!")