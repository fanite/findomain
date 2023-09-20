import yaml


def load_config(file_path):
    with open(file_path, "r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)
    return config
