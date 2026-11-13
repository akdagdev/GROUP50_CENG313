"""Shared utilities (seeding, metrics, submission writing)."""
import random
from pathlib import Path

import numpy as np
import pandas as pd

from src.data import TARGET_COLS


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)


def save_submission(ids, probabilities, path) -> Path:
    """Write predictions in the competition format: id + one probability per class."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    submission = pd.DataFrame(probabilities, columns=TARGET_COLS)
    submission.insert(0, "id", list(ids))
    submission.to_csv(path, index=False)
    return path
