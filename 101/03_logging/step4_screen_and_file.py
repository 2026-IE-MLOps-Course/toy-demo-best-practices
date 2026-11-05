# Step 4: the same lines go to the screen and to a file
import logging
from pathlib import Path  # new

FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
Path("logs").mkdir(exist_ok=True)  # new
screen = logging.StreamHandler()  # new: destination 1, the terminal
file = logging.FileHandler("logs/churn.log", encoding="utf-8")  # new: destination 2, a file
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S", handlers=[screen, file]  # new
)
logger = logging.getLogger("churn")

hours = 8.0
threshold = 10.0

logger.debug("Threshold is %.1f", threshold)
logger.info("Checking a customer with %.1f h", hours)
if hours < threshold:
    logger.warning("%.1f h -> churn", hours)
else:
    logger.info("%.1f h -> stay", hours)
