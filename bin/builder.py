import config.config as config
import bin.utilities as util


class Builder:
    def __init__(self, platform_name: str, env: dict):
        self.data = {
            'env': env,
            'OS': config.platform[platform_name],
            'project': config.project,
            'assets': config.assets,
            'docker': config.docker
        }

    def __set_env(self, env: dict) -> None:
        self.data['env'] = env

    def __set_project_root_path(self) -> None:
        self.data['project']['root_path'] = \
            self.data['env']['workbench_absolute_path'] \
            + self.data['env']['project_name'] \
            + '/'

    def __set_project_root_app_path(self) -> None:
        self.data['project']['app_path'] = \
            self.data['project']['root_path'] \
            + self.data['docker']['project_dir'] \
            + '/'

    def __set_assets_path(self) -> None:
        php_ver = self.data['env']['php_version']
        assets_root_path = self.data['assets']['root_path']

        self.data['assets']['path'] = assets_root_path + php_ver + '/'

    def __set_docker_container_names(self) -> None:
        container_names = self.data['env']['container_names']

        for key in container_names:
            container_names[key] += '-' + self.data['env']['project_name']

    def __handle_setters(self) -> None:
        self.__set_project_root_path()
        self.__set_project_root_app_path()
        self.__set_assets_path()
        self.__set_docker_container_names()

    def __handle_project_directory(self) -> None:
        # create simple project directory
        util.create_project_directory(
            self.data['project']['root_path']
        )
        # clone docker-lamp-stack repo from github
        util.clone_docker_repo(
            self.data['docker']['repo_url'],
            self.data['project']['root_path'],
            self.data['env']['php_version_branch']
        )
        # place proper project from given URL source
        util.place_project_from_repo(
            self.data['project']['app_path'],
            self.data['env']['project_repo_url']
        )

    def __copy_docker_environment_files(self) -> None:
        php_ver = self.data['env']['php_version']
        project_root_path = self.data['project']['root_path']
        assets_path = self.data['assets']['path']
        asset = self.data['assets'][php_ver]
        docker = self.data['docker']

        # copy .env to docker project
        util.copy_assets_file_to_docker_project(
            assets_path + asset['env'],
            project_root_path
        )

        # copy docker-compose.yml to docker project
        util.copy_assets_file_to_docker_project(
            assets_path + asset['docker_compose'],
            project_root_path
        )

        # copy webserver dockerfile to docker project
        util.copy_assets_file_to_docker_project(
            assets_path + asset['bin']['webserver']['dockerfile'],
            project_root_path + docker['bin']['webserver']['dockerfile']
        )

        # copy php.ini to docker project
        util.copy_assets_file_to_docker_project(
            assets_path + asset['config']['php']['php_ini'],
            project_root_path + docker['config']['php']['php_ini']
        )

    def __handle_docker_compose_environment(self) -> None:
        docker = self.data['docker']
        project_root = self.data['project']['root_path']

        # append variables to docker-compose .env file
        util.append_to_file_keys_values(
            project_root + docker['env'],
            self.data['env']['ports']
        )

        util.append_to_file_keys_values(
            project_root + docker['env'],
            self.data['env']['container_names']
        )

        # append variables to php_ini file
        util.append_to_file_keys_values(
            project_root + docker['config']['php']['php_ini'],
            self.data['OS']['php_ini']
        )

    def __handle_hosts_route_pointers(self) -> None:
        localhost_ip = self.data['env']['localhost_ip']
        domain_local = self.data['env']['domain_local']
        hosts_data = {
            localhost_ip: domain_local
        }

        # add pointers to hosts file
        util.append_to_file_keys_values(
            self.data['OS']['hosts_file_path'],
            hosts_data,
            ' '
        )

    def start(self) -> None:
        # set some constructor data props
        self.__handle_setters()

        # handle project directory & repos manipulation
        self.__handle_project_directory()

        # copy proper docker files from assets
        self.__copy_docker_environment_files()

        # make some changes to docker files
        self.__handle_docker_compose_environment()

        # handle local route pointers
        # self.__handle_hosts_route_pointers()
