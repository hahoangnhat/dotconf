import os
import shutil
from utils import logging

logger = logging.getLogger("dotconf")


def create_links(links):
    """Create symbolic links"""
    for symlink, source in links.items():
        BASE_DIRECTORY = os.environ.get("BASE_DIRECTORY")
        symlink = os.path.expanduser(symlink)

        if (
            source == None
            or not source
            or (
                isinstance(source, dict)
                and (source["path"] == None or not source["path"])
            )
        ):
            # Set default path
            source = os.path.join(
                BASE_DIRECTORY, symlink.split("/")[len(symlink.split("/")) - 1]
            )
        else:
            # Source is string
            if isinstance(source, str):
                # Fullpath
                if not os.path.exists(source):
                    # Only filename
                    if not os.path.exists(os.path.join(BASE_DIRECTORY, source)):
                        logger.info(f"Source path not exist: {source}")
                        continue
                    else:
                        source = os.path.join(BASE_DIRECTORY, source)
            # Source is dictionary
            elif isinstance(source, dict):
                # Fullpath
                if not os.path.exists(source["path"]):
                    # Only filename
                    if not os.path.exists(os.path.join(BASE_DIRECTORY, source["path"])):
                        logger.info(f"Source path not exist: {source}")
                        continue
                    else:
                        source["path"] = os.path.join(BASE_DIRECTORY, source["path"])

        # Overwrite links
        try:
            if os.path.islink(symlink):
                if os.environ.get("OVERWRITE").lower() == "true" or (
                    isinstance(source, dict) and source["overwrite"]
                ):
                    os.unlink(symlink)
            elif os.path.exists(symlink):
                if os.environ.get("OVERWRITE").lower() == "true" or (
                    isinstance(source, dict) and source["overwrite"]
                ):
                    if os.path.isfile(symlink):
                        os.remove(symlink)
                    elif os.path.isdir(symlink):
                        shutil.rmtree(symlink)
        except:
            logger.warning(f"Cannot overwrite symlink: {symlink}")

        # Create symbolic links
        create_parent_folder(symlink)
        if isinstance(source, str):
            os.symlink(source, symlink, target_is_directory=os.path.isdir(source))
            logger.info(f"Create symbolic link: {symlink} -> {source}")
        elif isinstance(source, dict):
            os.symlink(
                source["path"],
                symlink,
                target_is_directory=os.path.isdir(source["path"]),
            )
            logger.info(f'Create symbolic link: {symlink} -> {source["path"]}')


def remove_links(links):
    """Remove symbolic links"""
    for symlink, source in links.items():
        if os.path.islink(os.path.expanduser(symlink)):
            os.unlink(os.path.expanduser(symlink))
            logger.info(f"Remove symbolic link: {symlink}")


def create_parent_folder(symlink):
    """Create parent folder if needed"""
    parent_folder = os.path.dirname(os.path.expanduser(symlink))
    if not os.path.exists(parent_folder):
        os.makedirs(parent_folder)
