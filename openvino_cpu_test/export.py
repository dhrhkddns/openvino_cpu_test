from ultralytics import YOLO

# YOLOv8n 모델 로드
model = YOLO('yolov8n.pt')  # 사전 학습된 모델을 로드합니다. 필요한 경우 경로를 수정하세요.

# 모델을 ONNX 형식으로 export
model.export(format='openvino',imgsz=640,half=False,batch=1)


