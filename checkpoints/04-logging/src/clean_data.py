import logging

logger = logging.getLogger(__name__)


def clean_data(df, feature):
    """Drop rows where the feature is missing and say how many went."""
    cleaned = df.dropna(subset=[feature])
    dropped = len(df) - len(cleaned)
    if dropped:
        logger.warning("Dropped %d row(s) with a missing %s", dropped, feature)
    return cleaned
