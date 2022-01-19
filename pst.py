import defopt, shutil, sys
from pathlib import Path
from distutils import dir_util

stored_file_path = Path("~/.config/cpy/cpy_history").expanduser()


def read_history(path):
    tmp = []

    with open(stored_file_path, "r") as file:
        fr = file.readlines()
        for line in fr:
            tmp.append(Path(line.strip()))

    return tmp


def main(dst, *, clear=False, verbose=False, force=False, preserve=False):
    """Pastes stored paths to destination

    :param str dst: Destination directory
    :param bool clear: Clears the copied files from history after copying
    :param bool verbose: Print what's happened
    :param bool force: Forces copying to destination, even if file exists there already.
    :param bool preserve: By default, copied files are removed from the history list. This option preserves their entries (in case you want to copy the same files to a different location). """
    if not stored_file_path.exists():
        print("Copy program hasn't been invoked yet")
        sys.exit(1)

    stored_file_paths = read_history(stored_file_path)

    if len(stored_file_paths) == 0:
        print("Nothing has been stored for copying yet")
        sys.exit(1)

    destination_path = Path(dst)
    if not destination_path.exists():
        print("Destination path doesn't exist")
        sys.exit(1)

    # track which files have been copied so far
    copied_list = []

    for path in stored_file_paths:
        dst = (destination_path / path.name)

        if not path.exists():
            print(str(path) + " does not exist")
            continue

        if dst.exists():
            if not force:
                print(str(path) + " being skipped, already exists at destination")
                continue
            else:
                if verbose:
                    print(str(path) + " already exists at destination")

        if path.is_dir():
            dir_util.copy_tree(path, str(dst), preserve_symlinks=1)
        else:
            shutil.copy2(path, dst, follow_symlinks=True)

        copied_list.append(path)
        if verbose:
            print(str(path) + " copied")

    if clear:
        open(stored_file_path, "w").close()
        if verbose:
            print("History cleared")
    elif not preserve:
        for item in copied_list:
            stored_file_paths.remove(item)
        with open(stored_file_path, "w") as file:
            for line in stored_file_paths:
                file.write(str(line) + "\n")


if __name__ == "__main__":
    defopt.run(main)
