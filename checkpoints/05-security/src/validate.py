import logging

logger = logging.getLogger(__name__)


def validate(df, required_columns, feature):
    """Check, never fix: raise a clear error."""
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df.empty:
        raise ValueError("No rows left to validate")
    negative = int((df[feature] < 0).sum())
    if negative:
        raise ValueError(
            f"{negative} row(s) have a negative {feature}; fix the source data"
        )
    logger.info("Validation passed: %d rows", len(df))
    return True
