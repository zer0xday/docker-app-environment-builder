def set_input(label: str, question=None) -> str:
    if question:
        if not __yes_or_no(question):
            return None

    value = input(label)

    while not value:
        value = input(label)

    return value.strip()


def __yes_or_no(question: str, default="no"):
    valid = {
        "yes": True,
        "y": True,
        "ye": True,
        "no": False,
        "n": False
    }

    if default is None:
        prompt = " [y/n]: "
    elif default == "yes":
        prompt = " [Y/n]: "
    elif default == "no":
        prompt = " [y/N]: "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        choice = input(question + prompt).lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with: 'y / yes' or 'n / no'")


def set_php_version_branch(php_version: str) -> str:
    return php_version + '.x'


def set_data_recursively(
        env: dict,
        labels: dict
) -> dict:
    data = {}

    for key, value in env.items():
        if isinstance(value, dict):
            data[key] = set_data_recursively(value, labels)
        else:
            if not value:
                data[key] = set_input(labels[key])
            else:
                data[key] = value

    return data
