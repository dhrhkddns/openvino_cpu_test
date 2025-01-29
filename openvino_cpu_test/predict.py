from ultralytics import YOLO

# YOLOv8n 모델 로드
model = YOLO(r'C:\Users\Administrator\Desktop\openvino_cpu_test\yolov8n_int8_openvino_model')  # export된 모델을 사용하려면 export된 형식에 맞는 로딩 방법을 사용하세요.

video_path = "human.mp4"

results = model.predict(source=video_path,show=True,verbose=True,imgsz=640)



