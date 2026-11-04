"""Data loading and preprocessing helpers."""
from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")


def load_train(path=DATA_DIR / "train.csv") -> pd.DataFrame:
    """Load the competition training set."""
    return pd.read_csv(path)


def load_test(path=DATA_DIR / "test.csv") -> pd.DataFrame:
    """Load the competition test set."""
    return pd.read_csv(path)
