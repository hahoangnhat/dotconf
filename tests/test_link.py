import os
import shutil
from plugins import link

DOTCONF_PROJECT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Set BASE_DIRECTORY
os.environ["BASE_DIRECTORY"] = os.path.join(
    DOTCONF_PROJECT_DIRECTORY, "tests", "sources"
)
EXPECT_FILE = os.path.join(os.environ.get("BASE_DIRECTORY"), "test.txt")
EXPECT_FOLDER = os.path.join(os.environ.get("BASE_DIRECTORY"), "test_folder")


def setup_function():
    # Create source file
    dirpath = os.path.join(os.path.dirname(__file__), "sources")
    if not os.path.exists(EXPECT_FOLDER):
        os.makedirs(EXPECT_FOLDER)

    filename = os.path.join(dirpath, "test.txt")
    with open(filename, "w") as file:
        file.write("Hello world")


def teardown_function():
    # Remove sources folder
    source_path = os.path.join(os.path.dirname(__file__), "sources")
    if os.path.exists(source_path):
        shutil.rmtree(source_path)

    # Remove links folder
    link_path = os.path.join(os.path.dirname(__file__), "links")
    if os.path.exists(link_path):
        shutil.rmtree(link_path)


# File - START
def test_source_file_is_none():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: None}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_source_file_is_empty():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: ""}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_source_file_is_only_name():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: "test.txt"}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_source_file_is_full_path():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: EXPECT_FILE}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_file_path_attribute_is_none():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: {"path": None}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_file_path_attribute_is_empty():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: {"path": ""}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_file_path_is_only_name():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: {"path": "test.txt"}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_file_path_attribute_is_full_path():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    links = {linkpath: {"path": EXPECT_FILE}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_default_overwrite_file():
    os.environ["OVERWRITE"] = "true"
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    os.makedirs(os.path.dirname(linkpath))
    os.symlink(EXPECT_FILE, linkpath)

    links = {linkpath: {"path": EXPECT_FILE}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_overwrite_file():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt")
    os.makedirs(os.path.dirname(linkpath))
    os.symlink(EXPECT_FILE, linkpath)

    links = {linkpath: {"path": EXPECT_FILE, "overwrite": True}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isfile(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FILE


def test_create_multiple_file_links():
    link1 = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test1.txt")
    link2 = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test2.txt")
    links = {link1: EXPECT_FILE, link2: EXPECT_FILE}
    link.create_links(links)

    assert os.path.islink(link1)
    assert os.path.isfile(os.readlink(link1))
    assert os.readlink(link1) == EXPECT_FILE
    assert os.path.islink(link2)
    assert os.path.isfile(os.readlink(link2))
    assert os.readlink(link2) == EXPECT_FILE


# File - END


# Folder - START
def test_source_folder_is_none():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: None}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_source_folder_is_empty():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: ""}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_source_folder_is_only_name():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: "test_folder"}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_source_folder_is_full_path():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: EXPECT_FOLDER}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_folder_path_attribute_is_none():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: {"path": None}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_folder_path_attribute_is_empty():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: {"path": ""}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_folder_path_is_only_name():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: {"path": "test_folder"}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_folder_path_attribute_is_full_path():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    links = {linkpath: {"path": EXPECT_FOLDER}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_default_overwrite_folder():
    os.environ["OVERWRITE"] = "true"
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    os.makedirs(os.path.dirname(linkpath))
    os.symlink(EXPECT_FOLDER, linkpath)

    links = {linkpath: {"path": EXPECT_FOLDER}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_overwrite_folder():
    linkpath = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder")
    os.makedirs(os.path.dirname(linkpath))
    os.symlink(EXPECT_FOLDER, linkpath)

    links = {linkpath: {"path": EXPECT_FOLDER, "overwrite": True}}
    link.create_links(links)

    assert os.path.islink(linkpath)
    assert os.path.isdir(os.readlink(linkpath))
    assert os.readlink(linkpath) == EXPECT_FOLDER


def test_create_multiple_folder_links():
    link1 = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder1")
    link2 = os.path.join(DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder2")
    links = {link1: EXPECT_FOLDER, link2: EXPECT_FOLDER}
    link.create_links(links)

    assert os.path.islink(link1)
    assert os.path.isdir(os.readlink(link1))
    assert os.readlink(link1) == EXPECT_FOLDER
    assert os.path.islink(link2)
    assert os.path.isdir(os.readlink(link2))
    assert os.readlink(link2) == EXPECT_FOLDER


# Folder - END


def test_remove_links():
    link1 = os.path.join(
        DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test.txt"
    )  # File
    link2 = os.path.join(
        DOTCONF_PROJECT_DIRECTORY, "tests", "links", "test_folder"
    )  # Folder
    link3 = os.path.join(
        DOTCONF_PROJECT_DIRECTORY, "tests", "links", "not_exist.txt"
    )  # Not exist file
    link4 = os.path.join(
        DOTCONF_PROJECT_DIRECTORY, "tests", "links", "not_exist"
    )  # Not exist folder
    links = {link1: EXPECT_FOLDER, link2: EXPECT_FOLDER}
    link.create_links(links)
    links = {
        link1: EXPECT_FOLDER,
        link2: EXPECT_FOLDER,
        link3: EXPECT_FILE,
        link4: EXPECT_FOLDER,
    }
    link.remove_links(links)

    assert not os.path.exists(link1)
    assert not os.path.exists(link2)
