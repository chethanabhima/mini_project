# Final Model Validation Report

## 1. Selected Model

Experiment A — Frozen ResNet18.

## 2. External Test Dataset

PlantDoc external-test subset.

Total images: 42.

## 3. Overall Results

| Metric | Result |
|---|---:|
| Accuracy | 59.52% |
| Macro F1-score | 56.53% |
| Correct predictions | 25 |
| Incorrect predictions | 17 |

## 4. Class-wise Results

| Class | Correct | Total |
|---|---:|---:|
| Bacterial Spot | 0 | 9 |
| Early Blight | 8 | 9 |
| Healthy | 7 | 8 |
| Mosaic Virus | 6 | 10 |
| Yellow Leaf Curl Virus | 4 | 6 |

Leaf Miner was not represented in the PlantDoc external-test subset.

## 5. Confusion Matrix

Class order:

1. Bacterial Spot
2. Early Blight
3. Healthy
4. Leaf Miner
5. Mosaic Virus
6. Yellow Leaf Curl Virus

| Actual / Predicted | Bacterial | Early | Healthy | Leaf Miner | Mosaic | Yellow |
|---|---:|---:|---:|---:|---:|---:|
| Bacterial Spot | 0 | 8 | 0 | 0 | 1 | 0 |
| Early Blight | 0 | 8 | 0 | 1 | 0 | 0 |
| Healthy | 0 | 0 | 7 | 1 | 0 | 0 |
| Leaf Miner | 0 | 0 | 0 | 0 | 0 | 0 |
| Mosaic Virus | 0 | 1 | 1 | 1 | 6 | 1 |
| Yellow Leaf Curl Virus | 0 | 0 | 2 | 0 | 0 | 4 |

## 6. Observations

- Early Blight achieved 8 correct predictions out of 9.
- Healthy achieved 7 correct predictions out of 8.
- Mosaic Virus achieved 6 correct predictions out of 10.
- Bacterial Spot was the weakest represented class, with no correct predictions.

## 7. Limitations

- The external dataset contains only 42 images.
- The class distribution is imbalanced.
- Leaf Miner is absent.
- Some source images have ambiguous or composite visual content.
- Results should not be interpreted as proof of field-level diagnostic accuracy.

## 8. Conclusion

Experiment A achieved 59.52% accuracy and 56.53% macro F1 on the selected PlantDoc external-test subset.

The results indicate that the model requires further investigation and improvement before any real-world diagnostic deployment.
