# Step 3: add time and source to every line
import logging

FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(level="INFO", format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

load_logger = logging.getLogger("load_data")  # one logger per part of the code
check_logger = logging.getLogger("validate")

load_logger.info("Loaded %d rows from %s", 12, "customers.csv")
check_logger.info("Validation passed: %d rows", 11)
