# Computer Vision ML Pipeline

![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24+-2496ED?style=flat&logo=docker&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.30+-326CE5?style=flat&logo=kubernetes&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

End-to-end Computer Vision and Machine Learning Pipeline — from image processing and object tracking to model deployment with Docker, Kubernetes, and cloud services.

## Overview

A comprehensive pipeline for CV/ML applications covering image preprocessing, model training, inference, and deployment. Designed for IoT and edge computing scenarios with real-time object tracking.

## What's Included

- **OpenCV 5.x** image processing (thresholding, color-space transforms, segmentation)
- **FastAPI** async model serving with Docker Compose orchestration
- **Seldon Core** model wrapper for Kubernetes-native ML deployment
- **CUDA** version detection utility (C++17)
- **Boto3** S3 file ingestion with sampling
- **Pytest** test suite with coverage

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

## Project Structure

```
cv-ml-pipeline/
├── fastAPI/              # FastAPI image processing service
│   ├── Dockerfile        # Python 3.11-slim base
│   ├── docker-compose.yaml
│   ├── main.py           # API endpoints
│   ├── farshid.py        # Image conversion utilities
│   └── requirements.txt
├── seldon/               # Seldon Core model wrapper
│   ├── Dockerfile        # Python 3.11-slim base
│   ├── Farshid.py        # Grayscale conversion model
│   └── requirements.txt
├── cuda/                 # CUDA version detection (C++17)
│   ├── CMakeLists.txt
│   └── main.cu
├── poetry_projcet/       # Poetry-managed Python project
│   ├── pyproject.toml    # Modern Python 3.11+ config
│   └── poetry_projcet/__init__.py
├── k8s/                  # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
├── tests/                # Pytest test suite
│   ├── test_image_processing.py
│   ├── test_fastapi_utils.py
│   ├── test_api.py
│   ├── test_seldon.py
│   └── test_poetry_project.py
├── .github/workflows/    # CI/CD
│   ├── ci.yml            # Test + lint + Docker build
│   └── windows-cuda-opencv.yml
├── s3_copy_files.py      # AWS S3 file ingestion
├── test.py               # OpenCV thresholding demo
└── README.md
```

## Quick Start

### Local Development

```bash
git clone https://github.com/pirahansiah/cv-ml-pipeline.git
cd cv-ml-pipeline
pip install -r fastAPI/requirements.txt
pytest tests/ -v
```

### Docker

```bash
cd fastAPI
docker-compose up --build
# API available at http://localhost:8080
# Swagger docs at http://localhost:8080/docs
```

### Test the API

```bash
# Using curl
curl -X POST http://localhost:8080/process \
  -H "Content-Type: application/json" \
  -d '{"data": "<base64-encoded-image>"}'
```

## Kubernetes Deployment

### Prerequisites

- Kubernetes cluster (1.28+)
- `kubectl` configured
- Docker images built and pushed to a registry

### Deploy

```bash
# Build and push Docker image
cd fastAPI
docker build -t ghcr.io/pirahansiah/cv-ml-pipeline:latest .
docker push ghcr.io/pirahansiah/cv-ml-pipeline:latest

# Deploy to Kubernetes
kubectl apply -f k8s/

# Verify
kubectl get pods -l app=cv-ml-api
kubectl get svc cv-ml-api
```

### Components

| Manifest | Purpose |
|----------|---------|
| `k8s/deployment.yaml` | 2-replica deployment with readiness/liveness probes |
| `k8s/service.yaml` | LoadBalancer service (port 80 -> 8000) |
| `k8s/hpa.yaml` | Auto-scales 2-10 pods at 70% CPU |

### Scale

```bash
# Manual scale
kubectl scale deployment cv-ml-api --replicas=5

# Check HPA
kubectl get hpa cv-ml-api
```

### GPU Workloads

For GPU-accelerated inference, add to the container spec:

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

## Image Processing

### Thresholding Methods

| Method | Use Case | Complexity |
|--------|----------|------------|
| Otsu's Binarization | Bimodal histograms | O(N) |
| Adaptive (Gaussian) | Varying illumination | O(N·k) |
| Multi-level | Complex scenes | O(N·L) |
| Learned (U-Net) | Complex segmentation | O(N) at inference |

## Tech Stack

| Category | Tools |
|----------|-------|
| **ML/DL** | PyTorch 2.x, Ultralytics, ONNX Runtime, TensorRT |
| **CV** | OpenCV 5.x, scikit-image, Pillow |
| **Serving** | FastAPI, Seldon Core, TorchServe |
| **Orchestration** | Kubeflow, Airflow |
| **Tracking** | MLflow, W&B, DVC |
| **Deployment** | Docker, Kubernetes, Helm |
| **Edge** | OpenVINO, TensorRT, CoreML, TFLite |

## Testing

```bash
# Run all tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=. --cov-report=term-missing

# Lint
ruff check .
```

## CI/CD

- **ci.yml**: Runs on push/PR — tests Python 3.11/3.12/3.13, lints with ruff, builds Docker images
- **windows-cuda-opencv.yml**: Builds CUDA executable on Windows with CUDA 12.4

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Run tests (`pytest tests/`)
4. Submit a pull request

## License

MIT License

---

## 12-Month Roadmap

### Q1 2026 (Months 1–3): Foundation Hardening

| Priority | Item | Status |
|----------|------|--------|
| P0 | Replace all Python 3.7 references with 3.11+ | Done |
| P0 | Migrate TF1 (1.15) dependencies to TF2/PyTorch 2.x | Done |
| P0 | Add pytest test suite with >80% coverage | Done |
| P0 | Modernize Dockerfiles (python:3.11-slim) | Done |
| P1 | Add ruff linting to CI pipeline | Done |
| P1 | Add K8s manifests (deployment, service, HPA) | Done |
| P2 | Add pre-commit hooks (ruff, mypy, trailing-whitespace) | |
| P2 | Add mypy strict type checking | |
| P2 | Set up DVC for dataset versioning | |

### Q2 2026 (Months 4–6): ML Pipeline Modernization

| Priority | Item | Status |
|----------|------|--------|
| P0 | Integrate Ultralytics YOLO11 for object detection | |
| P0 | Add ONNX Runtime export for edge deployment | |
| P1 | Set up MLflow experiment tracking | |
| P1 | Add TensorRT export pipeline | |
| P1 | Create Kubeflow pipeline definitions | |
| P2 | Add SAM-2 integration for video segmentation | |
| P2 | Add Super-Resolution preprocessing (Real-ESRGAN) | |

### Q3 2026 (Months 7–9): Production & Observability

| Priority | Item | Status |
|----------|------|--------|
| P0 | Add Prometheus metrics + Grafana dashboards | |
| P0 | Implement structured logging (structlog) | |
| P0 | Add Helm chart for K8s deployment | |
| P1 | Set up model A/B testing framework | |
| P1 | Add OpenTelemetry distributed tracing | |
| P1 | Container scanning (Trivy) in CI | |
| P2 | Add Seldon v2 wrapper with V2 protocol | |

### Q4 2026 (Months 10–12): Edge & Advanced Features

| Priority | Item | Status |
|----------|------|--------|
| P0 | OpenVINO export for Intel edge devices | |
| P0 | CoreML export for Apple Silicon | |
| P1 | Add CLIP-guided adaptive preprocessing | |
| P1 | Real-time streaming inference (gRPC) | |
| P1 | Multi-camera tracking pipeline | |
| P2 | TFLite export for mobile deployment | |
| P2 | Add LangChain integration for vision QA | |

### Success Metrics

| Metric | Current | Target (12 mo) |
|--------|---------|-----------------|
| Test coverage | 0% | >85% |
| Python version | 3.7 (mixed) | 3.11+ (uniform) |
| Docker base images | EOL 3.7 | 3.11-slim |
| CI pipelines | 1 (build only) | 3 (test, lint, build) |
| K8s manifests | 0 | 3 (deploy, svc, HPA) |
| Edge formats | 0 | 4 (ONNX, TRT, OV, CoreML) |
