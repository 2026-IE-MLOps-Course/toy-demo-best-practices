# Step 5 (optional): each destination keeps its own level
import logging
from pathlib import Path

FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

Path("logs").mkdir(exist_ok=True)
formatter = logging.Formatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

screen = logging.StreamHandler()
screen.setLevel("WARNING")  # screen: problems only
file = logging.FileHandler("logs/detail.log", mode="w", encoding="utf-8")
file.setLevel("DEBUG")  # file: everything
screen.setFormatter(formatter)
file.setFormatter(formatter)

logging.basicConfig(level="DEBUG", handlers=[screen, file])
logger = logging.getLogger("main")

logger.debug("Predicting with threshold 10.0")
logger.info("Loaded 12 rows")
logger.warning("Dropped 1 row with a missing value")
