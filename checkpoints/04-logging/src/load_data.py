import logging

import pandas as pd

logger = logging.getLogger(__name__)


def load_data(path):
    df = pd.read_csv(path)
    logger.info("Loaded %d rows from %s", len(df), path.name)
    return df
