# Step 2: each print becomes a log message with a level
import logging  # new

LEVEL = "INFO"  # new: try "DEBUG", then "WARNING"
logging.basicConfig(level=LEVEL, format="%(levelname)s | %(message)s")  # new
logger = logging.getLogger("churn")  # new

hours = 8.0
threshold = 10.0

logger.debug("Threshold is %.1f", threshold)  # new: detail for developers
logger.info("Checking a customer with %.1f h", hours)  # new: normal progress
if hours < threshold:
    logger.warning("%.1f h -> churn", hours)  # new: needs attention
else:
    logger.info("%.1f h -> stay", hours)
