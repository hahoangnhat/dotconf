import os
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
from utils import file
from plugins import link, clean


def add_options(parser):
    parser.add_argument("-d", "--directory", help="Dotfile's base directory")
    parser.add_argument("-c", "--config", help="Configuration filepath")
    parser.add_argument("-a", "--action", help="Action")


def main():
    parser = ArgumentParser(RawTextHelpFormatter)
    add_options(parser)
    args = parser.parse_args()

    # Add base directory to env
    os.environ["BASE_DIRECTORY"] = args.directory

    # Load file config
    config = file.load(args.config)

    # Default
    if config["default"] != None or config["default"]:
        default = config["default"]
        # Overwrite
        if default["overwrite"] != None or default["overwrite"]:
            os.environ["OVERWRITE"] = default["overwrite"]

    # Clean
    if config["clean"] != None or config["clean"]:
        for path in config["clean"]:
            clean.remove_dead_links(path)

    # Links
    if config["links"] != None or config["links"]:
        links = config["links"]

        match args.action:
            case "install":
                link.create_links(links)
                logging.warning("Setup done")
            case "uninstall":
                link.remove_links(links)
                logging.warning("Uninstall done")
