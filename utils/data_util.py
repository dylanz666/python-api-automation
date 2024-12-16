import os
import json
import jsonpath
from utils.config_util import ConfigUtil


class DataUtil:
    root_path = os.getcwd()

    def __init__(self) -> None:
        pass

    @classmethod
    def get_data(cls, file_name):
        env = ConfigUtil.get_env()
        with open(os.path.join(cls.root_path, f"data/{env}/{file_name}.json"), "r") as f:
            data = json.load(f)
        return data

    @classmethod
    def get_data_by_jsonpath(cls, file_name, json_path):
        env = ConfigUtil.get_env()
        with open(os.path.join(cls.root_path, f"data/{env}/{file_name}.json"), "r") as f:
            data = json.load(f)
        return jsonpath.jsonpath(data, f"$.{json_path}")


if __name__ == "__main__":
    pass
