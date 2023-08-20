import time
import os
import logging
from enum import Enum, unique


@unique
class LogType(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    DEBUG = "DEBUG"
    CRITICAL = "CRITICAL"


class Logger:
    if not os.path.exists(os.getcwd() + '/log'):
        os.mkdir(os.getcwd() + '/log')

    log_filename = os.path.join(
        os.getcwd(), f"log/{time.strftime('%Y-%m-%d', time.localtime())}.log")
    logger = logging.getLogger()

    def __int__(self):
        pass

    def format_log_info(*info):
        info_list = []
        for info_item in info:
            info_list.append(info_item)
        return ' '.join(info_list)

    def set_basic_logging_config(log_type) -> None:
        logging.basicConfig(filename=Logger.log_filename, level=logging.DEBUG,
                            format=f'%(asctime)s [{log_type.value}] %(message)s', datefmt='[%Y-%m-%d %H:%M:%S]')

    def print_log(log_type, log_info) -> None:
        print(time.strftime("[%Y-%m-%d %H:%M:%S]",
              time.localtime()), f"[{log_type.value}]", log_info)

    def print_and_log(log_type, *info) -> None:
        Logger.set_basic_logging_config(log_type)

        log_info = Logger.format_log_info(*info)

        Logger.print_log(log_type, log_info)

        Logger.logger.info(log_info)

    @classmethod
    def info(cls, *info) -> None:
        cls.print_and_log(LogType.INFO, *info)

    @classmethod
    def warn(cls, *info) -> None:
        cls.print_and_log(LogType.WARN, *info)

    @classmethod
    def error(cls, *info) -> None:
        cls.print_and_log(LogType.ERROR, *info)

    @classmethod
    def debug(cls, *info) -> None:
        cls.print_and_log(LogType.DEBUG, *info)

    @classmethod
    def critical(cls, *info) -> None:
        cls.print_and_log(LogType.CRITICAL, *info)


if __name__ == "__main__":
    Logger.info("dylan, test", "some other log...")
