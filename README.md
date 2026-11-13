# GROUP50_CENG313

CENG313 Introduction to Data Science (Gazi University, Fall 2026-27). Kaggle project for Group 50.

## Team

| Name | Student ID | GitHub |
|---|---|---|
| Abdullah Akdağ | 23118080052 | [@akdagdev](https://github.com/akdagdev) |
| Cemal Berkay Bağrıaçık | 23118080042 | [@cemoal](https://github.com/cemoal) |

## Competition

[LLM Classification Finetuning](https://www.kaggle.com/competitions/llm-classification-finetuning). Each row contains a user prompt and the responses of two large language models; a human chose the preferred response or declared a tie. The task is to predict the probability of three outcomes: model A wins, model B wins, or tie. Submissions are scored with multi-class log loss (lower is better). It is an ongoing Code Competition with a rolling leaderboard: submissions are made from Kaggle notebooks and scored on a hidden test set. The test data contains only the prompt and the two responses, not the model names, so model names cannot be used as features.

## Dataset

The data files are downloaded from Kaggle and stored in data/, which is excluded from Git.

train.csv contains 57,477 rows and 9 columns: id, model_a, model_b, prompt, response_a, response_b, winner_model_a, winner_model_b and winner_tie. Each row compares two model conversations for the same prompts. Questions and responses are stored as JSON lists, allowing multiple turns per conversation.

The three target classes are model A wins, model B wins and tie. Exactly one target column is 1 in each training row.

The downloaded test.csv contains 3 example rows with id, prompt, response_a and response_b. sample_submission.csv shows the required output format: id and the predicted probabilities for the three target classes.

## Approach

- **Assignment 1 (EDA and baseline):** `assignment1_eda_baseline.ipynb`. Data overview and quality checks, exploratory analysis of the target and response lengths, preprocessing, and two baselines (class proportions, and response length with logistic regression).
- **Assignment 2 (proposed solution):** `assignment2_solution.ipynb`. TODO.

## How to run

1. Open the notebook in Google Colab.
2. Download the competition data from Kaggle into `data/` (not committed).
3. Install the packages with `pip install -r requirements.txt` (Colab already has most of them).
4. Run all cells (Restart & Run All). Shared code is imported from `src/`.

## Results (Assignment 1)

Both baselines are evaluated with log loss on the same stratified 80/20 split of `train.csv` (random seed 42).

| Baseline | Validation log loss |
| --- | ---: |
| Class proportions | 1.0972 |
| Response length + logistic regression | 1.0709 |

Kaggle public score of the submitted length baseline (`kaggle_submission.ipynb`): **1.07607** log loss, close to the validation score of 1.0709. Score evidence: `submissions/`.

## Progress log

| Date        | Who      | What                                                                    |
| ----------- | -------- | ----------------------------------------------------------------------- |
| 2 Nov 2026  | Abdullah | Repository created.                                                     |
| 4 Nov 2026  | Abdullah | Project structure: README, both notebooks, `src/` helpers.              |
| 4 Nov 2026  | Cemal    | Response length EDA and the first baseline models.                      |
| 7 Nov 2026  | Abdullah | Data quality analysis (missing values, duplicates).                     |
| 9 Nov 2026  | Abdullah | More data quality checks, more visuals, data overview, general cleanup. |
| 10 Nov 2026 | Cemal    | EDA and baseline conclusions.                                           |
| 13 Nov 2026 | Abdullah | `src/` refactor, README update, Kaggle submission screenshots.          |

Next: Assignment 2 (text features and a stronger model, compared against the baselines above).

## Kaggle submission history

| # | Notebook | Model | Public score (log loss) | Evidence |
|---|---|---|---|---|
| 1 | `kaggle_submission.ipynb` (Kaggle notebook version 5) | Response length features + logistic regression, fitted on all labelled rows | **1.07607** | `submissions/kaggle_score_public.png`, `submissions/kaggle_notebook_v5.png` |

Earlier notebook versions (1 to 4) were development runs on Kaggle and were not submitted. For comparison, our held-out validation log loss for the same model was 1.0709 and a uniform prediction gives ln 3 = 1.0986.

## Repository structure

```
GROUP50_CENG313/
├── README.md
├── requirements.txt
├── .gitignore                         data/ is not committed
├── assignment1_eda_baseline.ipynb     Assignment 1: EDA and baseline
├── assignment2_solution.ipynb         Assignment 2: improved solution (TODO)
├── src/
│   ├── data.py                        loading, word counts, features, target, split
│   ├── models.py                      baseline models
│   └── utils.py                       seeding, submission writing
├── data/                              competition data (not committed)
└── submissions/                       submission file and score screenshots
```
