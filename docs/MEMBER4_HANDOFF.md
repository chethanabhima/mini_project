# Member 4 — Project Handoff

## 1. Handoff Objective

Continue development using the frozen Experiment A ResNet18 checkpoint.

The training and model-selection phase has been completed. The next work should build on the selected model rather than repeat the existing experiments.

## 2. Required Files

- `models/final_selected_resnet18.pth`
- `dataset/manifests/plantdoc_external_test.csv`
- `experiments/plantdoc_error_analysis.csv`
- `docs/MODEL_CARD.md`
- `docs/FINAL_VALIDATION_REPORT.md`
- `requirements.txt`

## 3. Model Architecture

- ResNet18
- Six output classes
- 11,179,590 total parameters
- Frozen checkpoint
- PyTorch implementation

## 4. Required Class Order

The output indices must be interpreted in exactly this order:

```python
CLASS_NAMES = [
    "bacterial_spot",
    "early_blight",
    "healthy",
    "leaf_miner",
    "mosaic_virus",
    "yellow_leaf_curl_virus"
]
```

Do not change the order when integrating the model into another application.

## 5. Final Validation Reference

The selected model was evaluated on 42 PlantDoc external-test images.

- Accuracy: 59.52%
- Macro F1: 56.53%
- Correct predictions: 25/42

Use the saved evaluation artifacts as the reference. Do not silently change the benchmark or remove difficult images.

## 6. Suggested Continuation Tasks

1. Load the frozen checkpoint and verify inference.
2. Measure CPU and GPU inference latency where available.
3. Measure model memory requirements.
4. Evaluate image preprocessing and input compatibility.
5. Investigate model export options such as ONNX.
6. Explore post-training quantization.
7. Compare model size, latency and accuracy before and after optimization.
8. Document all changes and benchmark results.
9. Ensure the original checkpoint remains preserved.

## 7. Rules

- Do not train on PlantDoc external-test images.
- Do not fine-tune the selected checkpoint without recording a new experiment.
- Do not change the class-index mapping.
- Do not overwrite the original checkpoint.
- Keep the original PlantDoc validation results available for comparison.
- Record any preprocessing changes and their effects.

## 8. Expected Deliverables

- Reproducible inference script.
- Benchmark results.
- Optimized model artifact, if applicable.
- Before-and-after comparison.
- Updated technical documentation.

## 9. Important Note

The 59.52% PlantDoc accuracy is a small-sample external evaluation result, not a production-readiness guarantee. Any deployment or optimization work must report this limitation.
