"""Read a file using try, except, else and finally."""


def read_file(file_name):
    file = None
    try:
        file = open(file_name, encoding="utf-8")
    except FileNotFoundError:
        content = "__NO_SUCH_FILE__"
    else:
        content = file.read()
    finally:
        if file is not None:
            file.close()
    return "__CONTENT_START__\n" + content.rstrip("\n") + "\n__CONTENT_END__"


if __name__ == "__main__":
    import sys
    print(read_file(sys.argv[1] if len(sys.argv) > 1 else "one_lined_file.txt"))
