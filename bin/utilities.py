import os
import shutil
import git.exc
from pathlib import Path
from git import Repo


def rollback_project_directory(
        project_root_path: str
) -> None:
    if not project_root_path.strip():
        return None

    if not os.path.isdir(project_root_path):
        return None

    try:
        os.rmdir(Path(project_root_path))
    except OSError as error:
        raise ValueError(error)


def create_project_directory(
        project_root_path: str
) -> None:
    try:
        os.makedirs(project_root_path)
    except OSError:
        raise ValueError(
            "Creation of the directory %s failed" % project_root_path
        )
    else:
        print('Project directory created successfully!')


def clone_docker_repo(
        docker_lamp_stack_repo_url: str,
        project_root_path: str,
        version_branch: str
) -> None:
    try:
        Repo.clone_from(
            docker_lamp_stack_repo_url,
            project_root_path,
            branch=version_branch
        )
    except git.exc.InvalidGitRepositoryError:
        raise ValueError(
            'Docker lamp stack URL is incorrect. \
            Check this out in config file!'
        )

    print('Docker-lamp-stack repository cloned successfully!')


def __remove_default_docker_lamp_stack_project_dir(
        dir_to_remove: str
) -> None:
    try:
        shutil.rmtree(dir_to_remove)
    except OSError as error:
        raise ValueError(error)


def place_project_from_repo(
        project_full_path: str,
        project_repo_url: str
) -> None:
    __remove_default_docker_lamp_stack_project_dir(project_full_path)

    try:
        Repo.clone_from(project_repo_url, project_full_path)
    except git.exc.InvalidGitRepositoryError:
        raise ValueError('Project repository URL is incorrect.')

    print('Project repository placed successfully!')


def copy_assets_file_to_docker_project(
        assets_file_path: str,
        project_root_path: str
) -> None:
    try:
        shutil.copy(assets_file_path, project_root_path)
    except OSError as error:
        raise ValueError(error)


def append_to_file_keys_values(
        file_path: str,
        variables_dict: dict,
        assignment_operator="="
) -> None:
    try:
        file = open(file_path, 'a')

        for key in variables_dict:
            string = key + assignment_operator + variables_dict[key] + '\n'
            file.write(string)

        file.close()
    except OSError as error:
        raise ValueError(error)

