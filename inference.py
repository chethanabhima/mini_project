#!/usr/bin/env python3
"""
Inference entry point for the frozen Experiment A ResNet18 tomato-leaf model.

Expected checkpoint:
    models/final_selected_resnet18.pth

IMPORTANT:
The class order below is the exact order used by the selected model.
The image transform below (Resize(256), CenterCrop(224), ImageNet
normalization) must match the transform used during the final validation.
The project handoff notes say this transform still needs confirmation against
the original Experiment A validation notebook before deployment.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import torch
from PIL import Image
from torchvision import models, transforms


CLASS_NAMES = [
    "bacterial_spot",
    "early_blight",
    "healthy",
    "leaf_miner",
    "mosaic_virus",
    "yellow_leaf_curl_virus",
]

# This is the standard ImageNet evaluation transform currently recorded for
# the project. Confirm it against the exact Experiment A validation code.
IMAGE_SIZE = 224
RESIZE_SIZE = 256
IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)


def build_model() -> torch.nn.Module:
    """Create the same ResNet18 classifier shape: 6 output classes."""
    model = models.resnet18(weights=None)
    model.fc = torch.nn.Linear(model.fc.in_features, len(CLASS_NAMES))
    return model


def extract_state_dict(checkpoint: Any) -> dict[str, torch.Tensor]:
    """Accept either a raw state_dict or common checkpoint dictionary formats."""
    if isinstance(checkpoint, dict):
        for key in ("state_dict", "model_state_dict", "model"):
            candidate = checkpoint.get(key)
            if isinstance(candidate, dict) and candidate:
                checkpoint = candidate
                break

    if not isinstance(checkpoint, dict) or not checkpoint:
        raise ValueError("Checkpoint does not contain a valid model state_dict.")

    # Remove common wrappers used by DataParallel or training frameworks.
    cleaned = {}
    for key, value in checkpoint.items():
        if not isinstance(key, str):
            continue
        new_key = key
        for prefix in ("module.", "model."):
            if new_key.startswith(prefix):
                new_key = new_key[len(prefix):]
        cleaned[new_key] = value

    return cleaned


def load_model(checkpoint_path: Path, device: torch.device) -> torch.nn.Module:
    if not checkpoint_path.is_file():
        raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")

    # weights_only=True is safer for state-dict checkpoints. Fall back for
    # older PyTorch versions that do not accept this argument.
    try:
        checkpoint = torch.load(
            checkpoint_path, map_location="cpu", weights_only=True
        )
    except TypeError:
        checkpoint = torch.load(checkpoint_path, map_location="cpu")

    state_dict = extract_state_dict(checkpoint)
    model = build_model()

    try:
        model.load_state_dict(state_dict, strict=True)
    except RuntimeError as exc:
