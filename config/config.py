project = {
    'root_path': '',
    'app_path': '',
}

framework = {
    'magento2': './bin/framework/magento2/',
    'laravel': './bin/framework/laravel/',
}

docker = {
    'repo_url': 'https://github.com/sprintcube/docker-compose-lamp.git',
    'project_dir': 'www',
    'env': '.env',
    'docker_compose': 'docker-compose.yml',
    'bin': {
        'webserver': {
            'dockerfile': 'bin/webserver/Dockerfile'
        }
    },
    'config': {
        'php': {
            'php_ini': 'config/php/php.ini'
        }
    }
}

assets = {
    'root_path': "./assets/",
    'path': '',
    '7.4': {
        'env': '.env',
        'docker_compose': 'docker-compose.yml',
        'bin': {
            'webserver': {
                'dockerfile': 'bin/webserver/Dockerfile',
            }
        },
        'config': {
            'php': {
                'php_ini': 'config/php/php.ini'
            }
        }
    },
    '7.3': {

    },
    '7.2': {

    },
    '7.1': {

    }
}

win = {
    'hosts_file_path': './hosts',
    'php_ini': {
        'xdebug.remote_enable': '1',
        'xdebug.remote_host': 'host.docker.internal',
        'xdebug.remote_port': '9000',
        'xdebug.remote_connect_back': '0',
        'xdebug.remote_log': '/tmp/xdebug.log'
    }
}

linux = {
    'hosts_file_path': '/etc/hosts',
    'php_ini': {
        'xdebug.remote_enable': '1',
        'xdebug.remote_host': 'host.docker.internal',
        'xdebug.remote_port': '9000',
        'xdebug.remote_connect_back': '1',
        'xdebug.remote_log': '/tmp/xdebug.log'
    }
}

macosx = {}

platform = {
    'win32': win,
    'darwin': macosx,
    'linux': linux
}
