from enum import Enum, unique


@unique
class Severity(Enum):
    # 阻塞缺陷（功能未实现，无法下一步）
    BLOKER = "blocker"
    # 严重缺陷（功能点缺失）
    CRITICAL = "critical"
    # 一般缺陷（边界情况，格式错误）
    NORMAL = "normal"
    # 次要缺陷（界面错误与ui需求不符）
    MINOR = "minor"
    # 轻微缺陷（必须项无提示，或者提示不规范）
    TRIVIAL = "trivial"
