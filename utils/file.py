import os
import yaml
import logging
from functools import reduce

logger = logging.getLogger("dotconf")


def load(filepath):
    """Read config file"""
    if not os.path.exists(os.path.expanduser(filepath)):
        logger.warning("Config file not found")

    with open(filepath, "r") as file:
        data = yaml.safe_load(file)
        if len(data) == 0:
            raise RuntimeError("Configuration file is empty")
        return data
