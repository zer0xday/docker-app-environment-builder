import sys
import bin.environment as environment
from env import env
from bin.labels import labels
from bin.builder import Builder as Builder
from config.config import platform as available_platforms


class Core:
    def __init__(self):
        self.platform = sys.platform
        self.data = {}

    def _handle_available_platform(self):
        if self.platform not in available_platforms:
            raise ValueError("Sorry, I cannot recognize your OS.")

    def start(self) -> None:
        # check used platform availability in config file
        self._handle_available_platform()

        # set data from user input or env dictionary to data object
        self.data = environment.set_data_recursively(env, labels)

        # set php version branch for docker-lamp-stack
        self.data['php_version_branch'] = environment.set_php_version_branch(
            self.data['php_version']
        )

        builder = Builder(
            self.platform,
            self.data
        )
        builder.start()
