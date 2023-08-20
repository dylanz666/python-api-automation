import os
import shutil


class FileUtil:
    def __init__(self) -> None:
        pass

    @staticmethod
    def read_lines(file_path):
        """
        按行读取文件内容
        :param file_path: 要读取的目标文件的路径
        :return: 读取出的内容列表
        """
        with open(file_path, "r+") as file:
            return file.readlines()

    @staticmethod
    def write_lines(file_path, lines):
        """
        按行写入文件
        :param file_path: 要写入的目标文件的路径
        :param lines: 要写入文件的数据列表，需要换行时，需要在列表元素中自行处理
        :return: 无
        """
        with open(file_path, "w+") as f:
            f.writelines(lines)

    @staticmethod
    def makedirs_if_not_exist(*paths):
        """
        当文件夹路径不存在时，新建文件夹
        :param paths: 要判断、新建文件夹的路径，可传多个
        :return: 无
        """
        for path in paths:
            if not os.path.exists(path):
                os.system(f"echo {path} 不存在，新建")
                os.makedirs(path)

    @staticmethod
    def remove_if_exist(*paths):
        """
        移除文件夹或文件
        :param paths: 要移除的文件夹或文件的路径，可传多个
        :return: 无
        """
        for path in paths:
            if not os.path.exists(path):
                continue
            os.system(f"echo {path} 存在，删除")
            if os.path.isdir(path):
                shutil.rmtree(path)
                continue
            if os.path.isfile(path):
                os.remove(path)

    @classmethod
    def list_all_files(cls, dir_path):
        """
        采用递归方式，列出文件夹下的所有文件目录与文件
        :param dir_path: 要罗列文件目录与文件的文件路径
        :return: 文件路径dir_path下的所有文件目录与文件路径列表
        """
        files = []
        file_list = os.listdir(dir_path)  # 列出文件夹下所有的目录与文件
        for file_path in file_list:
            path = os.path.join(dir_path, file_path)
            if os.path.isdir(path):
                files.extend(cls.list_all_files(path))
            if os.path.isfile(path):
                files.append(path)
        return files

    @staticmethod
    def get_root_dir_path():
        return os.getcwd()


if __name__ == "__main__":
    pass
