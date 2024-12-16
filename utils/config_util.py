import os
import configparser
from pr_properties.properties import Properties


class ConfigUtil:
    root_path = os.getcwd()
    config = configparser.ConfigParser()

    def __init__(self) -> None:
        pass

    @classmethod
    def get_env(cls):
        properties = Properties()
        config_path = os.path.join(cls.root_path, "environment.properties")
        properties.read(path=config_path)
        return properties['env']

    @classmethod
    def get_config(cls, section, config_name):
        env = cls.get_env()
        config_path = os.path.join(cls.root_path, f"config/{env}.ini")
        cls.config.read(config_path, encoding="utf-8")
        return cls.config.get(section, config_name)

    @classmethod
    def get_config_in_file(cls, file_name, section, config_name):
        config_path = os.path.join(cls.root_path, f"config/{file_name}.ini")
        cls.config.read(config_path, encoding="utf-8")
        return cls.config.get(section, config_name)

    @classmethod
    def get_config_items_in_file(cls, file_name, section):
        config_path = os.path.join(cls.root_path, f"config/{file_name}.ini")
        cls.config.read(config_path, encoding="utf-8")
        return cls.config.items(section)


if __name__ == "__main__":
    pass
