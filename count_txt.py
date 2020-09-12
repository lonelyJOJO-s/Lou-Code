import os
import sys


def parse_file(path):
    file = open(path)
    i = 0
    tabs = 0
    spaces = 0
    for i, line in enumerate(file):
        tabs += line.count('\t')
        spaces += line.count(' ')
    file.close()
    return spaces, tabs, i + 1


def main(path):
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("spaces:{}. tabs:{}. lines:{}".format(spaces, tabs, lines))
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
