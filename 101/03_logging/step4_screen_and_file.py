# Step 4: send the same lines to the screen and to a file
import logging
from pathlib import Path

FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

Path("logs").mkdir(exist_ok=True)
formatter = logging.Formatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

screen = logging.StreamHandler()  # destination 1: the terminal
file = logging.FileHandler("logs/demo.log", encoding="utf-8")  # destination 2: a file
screen.setFormatter(formatter)
file.setFormatter(formatter)

logging.basicConfig(level="INFO", handlers=[screen, file])
logger = logging.getLogger("main")

logger.info("Loaded %d rows", 12)
logger.warning("Dropped %d row with a missing value", 1)
