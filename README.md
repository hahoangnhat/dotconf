# Dotconf
Dotconf is designed to be lightweight with no dependencies installation required. It provides a simple way to bootstrap your dotfiles repository, assuming that you already have one in place.

---
## Required
As Dotconf is written in Python, the only requirement for using it is to have Python 3.11 installed.

## Getting started
**Installation**

To utilize this tool, simply add it as a submodule to your current dotfiles repository:
```bash
cd ./dotfiles #replace this path with your real dotfiles's folder path
git submodule add https://github.com/hahoangnhat/dotconf.git dotconf
git config -f .gitmodules submodule.dotconf.ignore dirty # ignore dirty commits in the submodule
cp dotconf/install .
touch config.yaml
```

## Inspiration
Dotconf owes a profound debt of gratitude to the author and contributors of [Dotbot][dotconf], whose brilliant work has been a constant source of inspiration and has greatly influenced the development of this tool. I sincerely appreciate their invaluable contributions and unwavering dedication to the field.

<!-- Links -->
[dotconf]: https://github.com/anishathalye/dotbot
