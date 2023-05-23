import os
import logging
from plugins import clean

DOTCONF_PROJECT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def have_dead_links(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            if os.path.islink(dir_full_path) and not os.path.exists(
                os.readlink(dir_full_path)
            ):
                logging.warn(f"Directory: {dir_full_path}")
                return False

        for filename in filenames:
            file_full_path = os.path.join(dirpath, filename)
            if os.path.islink(file_full_path) and not os.path.exists(
                os.readlink(file_full_path)
            ):
                logging.warn(f"File: {file_full_path}")
                return False
    return True


def setup_function():
    # Create dead link
    dirpath = os.path.dirname(__file__)
    filepath = os.path.join(dirpath, "deadlink.txt")
    linkpath = os.path.join(dirpath, "deadlink.link")
    with open(filepath, "w") as file:
        file.write("Hello world")

    os.symlink(filepath, linkpath)
    os.remove(filepath)


def test_clean():
    clean.remove_dead_links(DOTCONF_PROJECT_DIRECTORY)
    assert have_dead_links(DOTCONF_PROJECT_DIRECTORY)
