# Step 6: log an error once, where you handle it
import logging

FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(level="INFO", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("main")

# A known problem: one clear line
try:
    raise ValueError("1 row has a negative usage_hours; fix the source data")
except ValueError as error:
    logger.error("Pipeline stopped: %s", error)

# An unexpected bug: the line plus the traceback
try:
    rate = 10 / 0
except Exception:
    logger.exception("Pipeline failed")
