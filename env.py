env = {
    ##########################################################################
    # Path to projects directory
    # Absolute path must ends with forward slash e.g '/home/user/projects/'
    # Windows path also must be transformed into forward slashes
    #
    'workbench_absolute_path': 'C:/Users/root/Desktop/workbench/',
    ##########################################################################
    # Project name must be inline string
    # e.g.: "example-project" or "example_project"
    #
    'project_name': 'zero-cmf',
    ##########################################################################
    # PHP Framework used in your project
    # If your project doesn't use any of given below
    # leave empty string or 'None' value type
    # Handled framework:
    #   Magento 2   - set to: 'magento2'
    #   Laravel     - set to: 'laravel'
    #
    # 'framework': None,
    ##########################################################################
    # Paste your URL to any existing git repository
    #
    'project_repo_url': 'https://github.com/zer0xday/zero-cmf.git',
    ##########################################################################
    # Available PHP versions for this script are: 7.4 | 7.3 | 7.2 | 7.1
    # the other ones will throw an error
    #
    'php_version': '7.4',
    ##########################################################################
    # Define your (not taken) ports for docker-compose .env file
    #
    'ports': {
        # HTTP port for PHP server e.g.: 3000
        'HOST_MACHINE_UNSECURE_HOST_PORT': '7111',
        # HTTPS port for php server e.g.: 443
        'HOST_MACHINE_SECURE_HOST_PORT': '713',
        # MySQL port e.g.: 3336
        'HOST_MACHINE_MYSQL_PORT': '3371',
        # phpMyAdmin port e.g.: 8080
        'PMA_HOST_PORT': '8087',
    },
    ##########################################################################
    # Docker container names defined in docker-compose.yml
    # You don't need to change any of them.
    # This script will automatically append your project name
    # to these existing ones
    #
    'container_names': {
        'WEBSERVER_CONTAINER_NAME': 'webserver',
        'MYSQL_CONTAINER_NAME': 'mysql',
        'PMA_CONTAINER_NAME': 'sc-phpmyadmin'
    },
    ##########################################################################
    # these variables are used to append a pointers to your 'hosts' file
    #
    'localhost_ip': '127.0.0.1',
    'domain_local': 'test.local',
}
