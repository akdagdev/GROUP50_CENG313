"""Baseline and proposed models."""
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler


def class_prior_probs(y_train, n_rows: int, n_classes: int = 3) -> np.ndarray:
    """Baseline 1: predict the training class proportions for every row."""
    proportions = np.bincount(y_train, minlength=n_classes) / len(y_train)
    return np.tile(proportions, (n_rows, 1))


def build_length_model():
    """Baseline 2: scaled length features + multinomial logistic regression."""
    # Sparse matrix operations avoid the macOS Accelerate matmul warning.
    return make_pipeline(
        StandardScaler(),
        FunctionTransformer(csr_matrix),
        LogisticRegression(),
    )
