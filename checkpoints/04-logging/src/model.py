def predict(usage, threshold=10.0):
    return (usage < threshold).astype(int)


def accuracy(y_true, y_pred):
    return (y_true == y_pred).mean()
