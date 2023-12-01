import yaml


def parse_worker_config():
    """Parses YAML file into dict.

    Returns:
        Dict: with key/vals from config.yaml
    """

    config_path = "./config.yaml"
    with open(config_path, "r") as f:  # type: ignore
        config_dict = yaml.safe_load(f)
        return config_dict
