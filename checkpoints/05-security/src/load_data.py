import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)


def load_data(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Raw data not found: {path}. Check paths.raw_data in config.yaml"
        )
    df = pd.read_csv(path)
    logger.info("Loaded %d rows from %s", len(df), path.name)
    return df
