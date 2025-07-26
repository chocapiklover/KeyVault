import os
import sys
from logic import init, add, unlock, lock, list, get, delete, update

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

        if sys.argv[1] == 'delete' and len(sys.argv) == 3:
            delete(sys.argv[2])

    
    

    if sys.argv[1] == 'delete' and len(sys.argv) == 3:
        delete(sys.argv[2])

    if sys.argv[1] == '--help':
        print("""
        Usage: python main.py [command] [options]

        Commands:
          init                Initialize the vault
          unlock              Unlock the vault
          lock                Lock the vault
          add                 Add a new service to the vault
          list                List all stored services
          get <service>      Retrieve credentials for a specific service
          delete <service>   Delete a specific service from the vault
          update <service>   Update a specific service from the vault

        Use 'python main.py --help' to see this message.
        """)
    if sys.argv[1] == "update" and len(sys.argv) == 3:
        update(sys.argv[2])
        return

print("Use '--help' to see valid commands")

if __name__ == "__main__":
    main()
