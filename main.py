import os
import sys
from logic import init, add, unlock, lock, list, get, delete

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "init":
            init()
            return 

        if sys.argv[1] == "unlock":
            unlock()
            return 
        if sys.argv[1] == "lock":
            lock()
            return 

        if sys.argv[1] == "add":
            add()
            return 
        
        if sys.argv[1] == "list":
            list()
            return 

        if sys.argv[1] == 'get' and len(sys.argv) == 3:
            get(sys.argv[2])
            return 

    print("Use '--help' to see valid commands")
    

    if sys.argv[1] == 'delete' and len(sys.argv) == 3:
        delete(sys.argv[2])


if __name__ == "__main__":
    main()
