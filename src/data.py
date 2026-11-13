"""Data loading and preprocessing helpers."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

DATA_DIR = Path("data")
TARGET_COLS = ["winner_model_a", "winner_model_b", "winner_tie"]


def load_train(path=DATA_DIR / "train.csv") -> pd.DataFrame:
    """Load the competition training set."""
    return pd.read_csv(path)


def load_test(path=DATA_DIR / "test.csv") -> pd.DataFrame:
    """Load the competition test set."""
    return pd.read_csv(path)


def word_count(turns_json: str) -> int:
    """Total number of words in a JSON-encoded list of conversation turns.

    Null turns (None) are skipped, so rows with missing turns still get a count.
    """
    turns = json.loads(turns_json)
    return sum(len(turn.split()) for turn in turns if isinstance(turn, str))


def length_features(df: pd.DataFrame) -> pd.DataFrame:
    """Response length features: words in A, words in B and their difference."""
    a_words = df["response_a"].map(word_count)
    b_words = df["response_b"].map(word_count)
    return pd.DataFrame({
        "a_words": a_words,
        "b_words": b_words,
        "word_diff": a_words - b_words,
    })


def encode_target(df: pd.DataFrame) -> np.ndarray:
    """Turn the three one-hot winner columns into one label: 0 = A, 1 = B, 2 = tie."""
    return df[TARGET_COLS].to_numpy().argmax(axis=1)


def stratified_split(y, test_size: float = 0.20, seed: int = 42):
    """Stratified train/validation split. Returns (train_idx, val_idx) row positions."""
    return train_test_split(
        np.arange(len(y)), test_size=test_size, random_state=seed, stratify=y
    )
