import os
import sys
from logic import init, add


def main():
    if sys.argv[1] == "init":
        init()

    if sys.argv[1] == "add":
        add()


if __name__ == "__main__":
    main()
