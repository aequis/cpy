import defopt, sys
from pathlib import Path

stored_file_path = Path("~/.config/cpy/cpy_history")
if stored_file_path.parts[0] == "~":
    stored_file_path = stored_file_path.expanduser()
if not stored_file_path.is_absolute():
    stored_file_path = stored_file_path.resolve()


def create_path(path):
    path.parents[0].mkdir(parents=True)
    path.touch()


def main(*file_paths, clear=False, verbose=False):
    """Store a file path for copying

    :param str file_paths: File path to be stored
    :param bool clear: Clear all stored file paths
    :param bool verbose: Print what's happened"""
    if not stored_file_path.exists():
        create_path(stored_file_path)

    if clear:
        open(stored_file_path, "w").close()
        if verbose:
            print("History cleared")

    for file_path in file_paths:
        file_path = Path(file_path)

        if not file_path.exists():
            print(str(file_path) + " doesn't exist")
            continue

        if not file_path.is_absolute():
            file_path = file_path.resolve()

        with open(stored_file_path, 'a') as file:
            file.write(str(file_path) + "\n")

        if verbose:
            print(str(file_path) + " stored")


if __name__ == "__main__":
    defopt.run(main)
