from pathlib import Path

COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    """Рекурсия яка по файловій системі ходить та показує в консолі"""
    if path.is_dir():

        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
        indent += "    " if prefix else ""

        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))


if __name__ == "__main__":
    root = Path("C:/Users/user/Desktop/Algorithms")
    display_tree(root)
