# Computer Vision ML Pipeline

![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24+-2496ED?style=flat&logo=docker&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

End-to-end Computer Vision and Machine Learning Pipeline — from image processing and object tracking to model deployment with Docker, Kubernetes, and cloud services.

## Overview

A comprehensive pipeline for CV/ML applications covering image preprocessing, model training, inference, and deployment. Designed for IoT and edge computing scenarios with real-time object tracking.

## What's New (2025-2026)

- **PyTorch 2.x** with `torch.compile()` for optimized inference
- **ONNX Runtime** for cross-platform edge deployment
- **TensorRT** integration for NVIDIA GPU acceleration
- **Ultralytics YOLO11** for real-time object detection
- **SAM-2** for video segmentation
- **OpenVINO** for Intel edge deployment
- **FastAPI** replacing Flask for async model serving
- **Kubeflow Pipelines** for ML orchestration
- **MLflow** for experiment tracking
- **DVC** for data versioning
- **Docker Compose** multi-service orchestration

## Architecture

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐
│  Data       │───▶│  Preprocess  │───▶│  Model       │
│  Ingestion  │    │  & Augment   │    │  Training    │
└─────────────┘    └──────────────┘    └──────┬───────┘
                                              │
┌─────────────┐    ┌──────────────┐    ┌──────▼───────┐
│  Edge       │◀───│  Model       │◀───│  MLflow      │
│  Deploy     │    │  Serving     │    │  Registry    │
└─────────────┘    └──────────────┘    └──────────────┘
```

## Image Processing

### Thresholding Methods

| Method | Use Case | Complexity |
|--------|----------|------------|
| Otsu's Binarization | Bimodal histograms | O(N) |
| Adaptive (Gaussian) | Varying illumination | O(N·k) |
| Multi-level | Complex scenes | O(N·L) |
| Fuzzy Thresholding | Noisy images | O(N·L²) |
| Entropy-based | License plates | O(N·L) |

### Modern Approaches (2025-2026)

- **Learned Thresholding**: U-Net/DeepLabV3+ for semantic segmentation
- **SAM-2**: Zero-shot segmentation with text prompts
- **CLIP-guided**: Text-image alignment for adaptive processing
- **Super-resolution**: Real-ESRGAN for upscaling before processing

## Object Tracking Pipeline

```python
# Modern tracking with YOLO11 + ByteTrack
from ultralytics import YOLO
from byte_tracker import ByteTrack

model = YOLO("yolo11x.pt")
tracker = ByteTrack(track_thresh=0.5, match_thresh=0.8)

results = model.track(source="video.mp4", tracker=True)
```

## Tech Stack

| Category | Tools |
|----------|-------|
| **ML/DL** | PyTorch 2.x, Ultralytics, ONNX Runtime, TensorRT |
| **CV** | OpenCV 4.9+, scikit-image, Pillow |
| **Serving** | FastAPI, TorchServe, Triton Inference Server |
| **Orchestration** | Kubeflow, Airflow, Prefect |
| **Tracking** | MLflow, W&B, DVC |
| **Deployment** | Docker, Kubernetes, Helm |
| **Edge** | OpenVINO, TensorRT, CoreML, TFLite |

## Image Processing Modules

### Thresholding

```python
import cv2
import numpy as np

# Otsu's thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Adaptive thresholding
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 11, 2)
```

### Modern Segmentation

```python
# SAM-2 for video segmentation
from segment_anything_2 import SAM2

sam = SAM2("sam2_hiera_large.pt")
masks = sam.segment(frame, points=points, labels=labels)
```

## Deployment

### Docker

```dockerfile
FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cv-inference
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cv-inference
  template:
    spec:
      containers:
      - name: cv-inference
        image: ghcr.io/cv-ml-pipeline:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

### Edge Deployment

```bash
# Export to ONNX
python export_onnx.py --model yolov9.pt --output yolov9.onnx

# Convert to TensorRT
trtexec --onnx=yolov9.onnx --saveEngine=yolov9.engine --fp16

# Deploy to edge device
python edge_inference.py --engine yolov9.engine --source camera.mp4
```

## Research References

- **U-Net** (2015): Convolutional Networks for Biomedical Image Segmentation — [Ronneberger et al.](https://arxiv.org/abs/1505.04597)
- **SAM-2** (2024): Segment Anything Model 2 for Video — [Meta AI](https://github.com/facebookresearch/segment-anything-2)
- **YOLO11** (2025): Real-time Object Detection — [Ultralytics](https://github.com/ultralytics/ultralytics)
- **ByteTrack** (2022): Multi-Object Tracking by Associating Every Detection — [Zhang et al.](https://arxiv.org/abs/2110.02033)
- **CLIP** (2021): Learning Transferable Visual Models — [OpenAI](https://arxiv.org/abs/2103.00020)
- **ONNX Runtime** (2024): Cross-platform ML inference — [Microsoft](https://onnxruntime.ai)
- **TensorRT** (2024): NVIDIA GPU inference optimization — [NVIDIA](https://developer.nvidia.com/tensorrt)

## Quick Start

```bash
git clone https://github.com/pirahansiah/cv-ml-pipline.git
cd cv-ml-pipline
docker-compose up --build
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License
