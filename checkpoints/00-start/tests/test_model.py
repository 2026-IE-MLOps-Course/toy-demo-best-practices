import pandas as pd
import src.model as model


def test_predict():
    assert model.predict(pd.Series([2.0, 15.0])).tolist() == [1, 0]
