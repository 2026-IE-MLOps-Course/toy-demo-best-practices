# Step 3: every line gets the time, the level and the source
import logging

FORMAT = "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
logging.basicConfig(level="INFO", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")  # new
logger = logging.getLogger(__name__)

# FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"  # new
# logging.basicConfig(level="INFO", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")  # new
# logger = logging.getLogger("churn")

hours = 8.0
threshold = 10.0

logger.debug("Threshold is %.1f", threshold)
logger.info("Checking a customer with %.1f h", hours)
if hours < threshold:
    logger.warning("%.1f h -> churn", hours)
else:
    logger.info("%.1f h -> stay", hours)
