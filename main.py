import os
import sys
from logic import init, add, unlock, lock, list

def main():
    if sys.argv[1] == "init":
        init()
    if sys.argv[1] == "unlock":
        unlock()
    if sys.argv[1] == "lock":
        lock()

    if sys.argv[1] == "add":
        add()
    
    if sys.argv[1] == "list":
        list()


if __name__ == "__main__":
    main()
