# Step 5: a bad value is logged once, as an ERROR
import logging
from pathlib import Path

FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
Path("logs").mkdir(exist_ok=True)
screen = logging.StreamHandler()
file = logging.FileHandler("logs/churn.log", encoding="utf-8")
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S", handlers=[screen, file]
)
logger = logging.getLogger("churn")

hours = -3.0  # new: a bad value
threshold = 10.0

try:  # new
    logger.debug("Threshold is %.1f", threshold)
    logger.info("Checking a customer with %.1f h", hours)
    if hours < 0:  # new
        raise ValueError(f"{hours} is a negative usage; fix the source data")  # new
    if hours < threshold:
        logger.warning("%.1f h -> churn", hours)
    else:
        logger.info("%.1f h -> stay", hours)
except ValueError as error:  # new
    logger.error("Stopped: %s", error)  # new
