import os
import yaml
import logging
from functools import reduce


def load(filepath):
    """Read config file"""
    if not os.path.exists(os.path.expanduser(filepath)):
        logging.error("Config file not found")

    with open(filepath, "r") as file:
        data = yaml.safe_load(file)
        if len(data) == 0:
            raise RuntimeError("Configuration file is empty")
        return reduce(lambda x, y: {**x, **y}, data)
