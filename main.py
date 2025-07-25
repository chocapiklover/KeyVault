import os
import sys
from logic import init, add
from logic import unlock
from logic import lock  

def main():
    if sys.argv[1] == "init":
        init()
    if sys.argv[1] == "unlock":
        unlock()
    if sys.argv[1] == "lock":
        lock()

    if sys.argv[1] == "add":
        add()


if __name__ == "__main__":
    main()
