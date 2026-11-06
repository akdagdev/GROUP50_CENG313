# GROUP50_CENG313

CENG313 Introduction to Data Science (Gazi University, Fall 2026-27). Kaggle project for Group 50.

## Team

| Name | Student ID | GitHub |
|---|---|---|
| Abdullah Akdağ | 23118080052 | [@akdagdev](https://github.com/akdagdev) |
| Cemal Berkay Bağrıaçık | 23118080042 | [@cemoal](https://github.com/cemoal) |

## Competition

[LLM Classification Finetuning](https://www.kaggle.com/competitions/llm-classification-finetuning). Given a prompt and two LLM responses (A and B), predict whether a human prefers A, prefers B, or rates them a tie. Submissions are three-class probabilities (`winner_model_a`, `winner_model_b`, `winner_tie`). Evaluation metric is multiclass log loss (lower is better).

## Dataset

TODO (fill after loading `train.csv` / `test.csv` locally or on Colab): number of rows, column list, and class balance for the three winner columns. Competition data is not committed; keep it under `data/`.

## Approach

- **Assignment 1 (EDA and baseline):** `assignment1_eda_baseline.ipynb`
  - Response length EDA: word counts for A vs B vs win/tie rates (Cemal, 4 Kas).
  - Baseline 1: stratified class-prior probabilities (validation log loss 1.0972).
  - Baseline 2: length features (`a_kelime`, `b_kelime`, `kelime_farki`) + logistic regression (validation log loss 1.0709).
  - Still open: data-quality checks (missing, duplicates, inconsistencies), more EDA/plots, written conclusions, Kaggle submission.
- **Assignment 2 (proposed solution):** `assignment2_solution.ipynb`. TODO.

## Results

| Model | Validation log loss | Kaggle public score |
|---|---|---|
| Class-prior baseline | 1.0972 | |
| Length features + logistic regression | 1.0709 | |

Scores are from a 80/20 stratified validation split (`random_state=42`) in `assignment1_eda_baseline.ipynb`.

## How to run

1. Open the notebook in Google Colab.
2. Download the competition data from Kaggle into `data/` (not committed).
3. Run all cells. Shared code is imported from `src/`.

## Repository layout

```
GROUP50_CENG313/
├── README.md
├── assignment1_eda_baseline.ipynb
├── assignment2_solution.ipynb
├── requirements.txt
└── src/
    ├── data.py
    ├── models.py
    └── utils.py
```

## Progress log

| Date | Member | Work done |
|---|---|---|
| 2026-11-02 | Abdullah | Repository created |
| 2026-11-04 | Abdullah | Repository renamed to GROUP50_CENG313, project structure added |
| 2026-11-04 | Cemal | Response-length EDA and two baselines (class prior 1.0972, length+LR 1.0709) |

## Kaggle submission history

| Date | Model | Public score | Notes |
|---|---|---|---|
| | | | |
