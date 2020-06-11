from bin.core import Core
from config.config import project
from bin.utilities import rollback_project_directory
import sys


def main():
    try:
        core = Core()
        core.start()
    except ValueError as error:
        print(error)
        print('Terminating...')
        rollback_project_directory(project['root_path'])
        sys.exit(0)

    print('Your project has been successfully created. Happy coding then ;)')
    sys.exit(0)


main()
