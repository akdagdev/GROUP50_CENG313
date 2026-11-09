# GROUP50_CENG313

CENG313 Introduction to Data Science (Gazi University, Fall 2026-27). Kaggle project for Group 50.

## Team

| Name | Student ID | GitHub |
|---|---|---|
| Abdullah Akdağ | 23118080052 | [@akdagdev](https://github.com/akdagdev) |
| Cemal Berkay Bağrıaçık | 23118080042 | [@cemoal](https://github.com/cemoal) |

## Competition

[LLM Classification Finetuning](https://www.kaggle.com/competitions/llm-classification-finetuning). TODO: one-paragraph description of the task and the evaluation metric.

## Dataset

The data files are downloaded from Kaggle and stored in data/, which is excluded from Git.

train.csv contains 57,477 rows and 9 columns: id, model_a, model_b, prompt, response_a, response_b, winner_model_a, winner_model_b and winner_tie. Each row compares two model conversations for the same prompts. Questions and responses are stored as JSON lists, allowing multiple turns per conversation.

The three target classes are model A wins, model B wins and tie. Exactly one target column is 1 in each training row.

The downloaded test.csv contains 3 example rows with id, prompt, response_a and response_b. sample_submission.csv shows the required output format: id and the predicted probabilities for the three target classes.

## Approach

- **Assignment 1 (EDA and baseline):** `assignment1_eda_baseline.ipynb`.
- **Assignment 2 (proposed solution):** `assignment2_solution.ipynb`. TODO.

## How to run

1. Open the notebook in Google Colab.
2. Download the competition data from Kaggle into `data/` (not committed).
3. Run all cells. Shared code is imported from `src/`.
