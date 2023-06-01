import os
import yaml
import logging
import logging.config

config_file = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "logging.yaml"
)

def getLogger(logger):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)

    return logging.getLogger(logger)
