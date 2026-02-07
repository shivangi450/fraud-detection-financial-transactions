"""Evaluation utilities (placeholder)."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Metrics:
    accuracy: float
    precision: float
    recall: float
    f1: float
    roc_auc: float
