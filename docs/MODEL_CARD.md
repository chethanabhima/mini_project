# Tomato Leaf Health Diagnosis and Management

## Project Overview

This project develops a six-class tomato leaf image classification system using a fine-tuned ResNet18 convolutional neural network.

The model is intended to classify tomato leaf images into the following categories:

1. Bacterial Spot
2. Early Blight
3. Healthy
4. Leaf Miner
5. Mosaic Virus
6. Yellow Leaf Curl Virus

## Current Model

- Architecture: ResNet18
- Framework: PyTorch
- Number of classes: 6
- Total parameters: 11,179,590
- Selected experiment: Experiment A
- Checkpoint: `models/final_selected_resnet18.pth`
- Checkpoint size: approximately 42.72 MB
- Model status: Frozen; no further training during deployment benchmarking.

## Class Index Mapping

| ID | Class |
|---:|---|
| 0 | bacterial_spot |
| 1 | early_blight |
| 2 | healthy |
| 3 | leaf_miner |
| 4 | mosaic_virus |
| 5 | yellow_leaf_curl_virus |

## Final External Validation

Dataset: PlantDoc external-test subset.

- Total images: 42
- Correct predictions: 25
- Accuracy: 59.52%
- Macro F1-score: 56.53%

PlantDoc class distribution:

| Class | Images |
|---|---:|
| Bacterial Spot | 9 |
| Early Blight | 9 |
| Healthy | 8 |
| Mosaic Virus | 10 |
| Yellow Leaf Curl Virus | 6 |

Leaf Miner is not represented in this external test subset.

## Important Limitations

- PlantDoc external test is small and class-imbalanced.
- External performance is not evidence of Karnataka-wide diagnostic accuracy.
- Model predictions are image classifications, not laboratory-confirmed diagnoses.
- The model has not been established as production-ready.

## Repository Guidance

Use the frozen selected checkpoint for inference and deployment experiments. Do not replace it with an experimental checkpoint without documenting and evaluating the change.
