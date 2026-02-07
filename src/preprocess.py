"""Preprocessing helpers.

Note: The primary, complete workflow lives in the Jupyter notebook in /notebooks.
These scripts are provided as a clean starting point if you want to productionize the pipeline.
"""
from __future__ import annotations
import pandas as pd

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Light cleaning: trim strings, standardize column names."""
    out = df.copy()
    out.columns = [c.strip().replace(" ", "_") for c in out.columns]
    obj_cols = out.select_dtypes(include=["object"]).columns
    for c in obj_cols:
        out[c] = out[c].astype(str).str.strip()
    return out
