import logging
import logging.config

logging.config.fileConfig("logging.yaml")
logger = logging.getLogger("dotconf")
