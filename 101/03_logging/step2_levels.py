# Step 2: five levels, from detail to disaster
import logging

LEVEL = "INFO"  # try "DEBUG", then "WARNING"

logging.basicConfig(level=LEVEL, format="%(levelname)s | %(message)s")
logger = logging.getLogger("demo")

logger.debug("Predicting with threshold 10.0")  # detail for developers
logger.info("Loaded 12 rows")  # normal progress
logger.warning("Dropped 1 row with a missing value")  # odd, but we continue
logger.error("Pipeline stopped: negative hours")  # this run failed
logger.critical("Disk full, cannot save results")  # the whole system is in trouble
