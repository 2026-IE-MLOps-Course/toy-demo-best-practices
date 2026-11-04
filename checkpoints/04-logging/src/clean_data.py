import logging

logger = logging.getLogger(__name__)


def clean_data(df, feature):
    cleaned = df.dropna(subset=[feature])
    dropped = len(df) - len(cleaned)
    if dropped:
        logger.warning("Dropped %d row(s) with a missing %s", dropped, feature)
    return cleaned
