import logging

logger = logging.getLogger(__name__)


def predict(usage, threshold=10.0):
    logger.debug("Predicting with threshold %.1f", threshold)
    return (usage < threshold).astype(int)


def accuracy(y_true, y_pred):
    return (y_true == y_pred).mean()
