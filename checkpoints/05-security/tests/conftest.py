"""Shared test data: small, fixed and fully in memory."""

import pandas as pd
import pytest


@pytest.fixture
def df_ok():
    return pd.DataFrame(
        {
            "customer_id": [1, 2, 3],
            "usage_hours": [2.0, 15.0, 8.0],
            "churned": [1, 0, 1],
        }
    )
