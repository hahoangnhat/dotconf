# Dotconf
Dotconf is designed to be lightweight with no dependencies installation required. It provides a simple way to bootstrap your dotfiles repository, assuming that you already have one in place.

> **Note:** Please note that the file README.md is still being edited and may undergo further changes.

## Required
As Dotconf is written in Python, the only requirement for using it is to have Python 3.11 installed.

## Installation

To utilize this tool, simply add it as a submodule to your current dotfiles repository:
```bash
cd ./dotfiles # replace this path with your real dotfiles's folder path
git submodule add https://github.com/hahoangnhat/dotconf.git dotconf
git config -f .gitmodules submodule.dotconf.ignore dirty # ignore dirty commits in the submodule
cp dotconf/install .
touch config.yaml # Create file config
```
## Setup file config

Dotconf uses YAML-formatted configuration files. In installation step above, we created a config.yaml file. This is a simple example of this file:
```yaml
default:
  overwrite: 'true'
clean: ['~']
links:
  ~/shell:
  ~/.zshrc:
```

In this example, Dotconf defines two tasks: **clean** and **links**. The **default** section sets the overwrite property to true for all links, allowing existing links to be overwritten if necessary.

### Configuration

**1. Links**

The **links** task in Dotconf specifies a list of symbolic links to be created. Each link is defined with the link's path as the key and the target path as the value. Here's an example:
```yaml
links:
  ~/shell: /usr/local/shell       # folder
  ~/.bashrc: ~/.bashrc            # file
```

If the target path is not specified, Dotconf will use the file/folder name in the link's path to search within the dotfiles repository. If the file or folder exists, a symbolic link will be created. If it doesn't exist, no symbolic link will be created.

For example, let's say the dotfiles repository is located at **/usr/local/dotfiles** and it contains a folder named **shell** (/usr/local/dotfiles/shell).

```yaml
links:
  ~/shell:
```

This is equivalent to:
```yaml
links:
  ~/shell: /usr/local/dotfiles/shell
```

Moreover, the value for a link in the configuration file can be a dictionary, allowing for more advanced settings. Here's an example:
```yaml
links:
  ~/shell:
    path: /usr/local/dotfiles/shell
    overwrite: True
```
In this example, the **path** property specifies the target path for the symbolic link, which can be a file or a folder.
The **overwrite** property is optional and set to True, enabling the overwrite of existing links if necessary.

**2. Clean**

The **clean** task in Dotconf helps you remove dead symbolic links in a directory and its subdirectories. You can specify an array of directory paths that you want to clean up, and Dotconf will take care of it. Here's an example:
```yaml
clean: ['/etc', '/usr/local']
```

Equivalent to:
```yaml
clean:
  - '/etc'
  - '/usr/local'
```

**3. Default**

The **default** section allows you to define default properties for the **links** task in the present configuration. Currently, it only includes the **overwrite** property, which is set to true for all links. This default property works similarly to the **overwrite** property in each individual link defined in the **links** task. It enables the overwriting of existing links if necessary.

## Inspiration
Dotconf owes a profound debt of gratitude to the author and contributors of [Dotbot][dotconf], whose brilliant work has been a constant source of inspiration and has greatly influenced the development of this tool. I sincerely appreciate their invaluable contributions and unwavering dedication to the field.

<!-- Links -->
[dotconf]: https://github.com/anishathalye/dotbot
