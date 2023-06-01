import os
from utils import logging

logger = logging.getLogger("dotconf")


def remove_dead_links(folder):
    """Remove dead symbolic links in given folder"""
    for dirpath, dirnames, filenames in os.walk(folder):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            if os.path.islink(dir_full_path) and not os.path.exists(
                os.readlink(dir_full_path)
            ):
                os.rmdir(dir_full_path)
                logger.info(f"Remove dead folder symbolic link: {dir_full_path}")

        for filename in filenames:
            file_full_path = os.path.join(dirpath, filename)
            if os.path.islink(file_full_path) and not os.path.exists(
                os.readlink(file_full_path)
            ):
                os.remove(file_full_path)
                logger.info(f"Remove dead file symbolic link: {file_full_path}")
        logger.info("Clean done!")
