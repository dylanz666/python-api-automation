import base64


class DesUtil:
    def __init__(self) -> None:
        pass

    @staticmethod
    def base64_encode(text):
        return base64.b64encode(text.encode()).decode()

    @staticmethod
    def base64_decode(text):
        return base64.b64decode(text).decode()


if __name__ == "__main__":
    assert DesUtil.base64_encode("dylan") == "ZHlsYW4="
    assert DesUtil.base64_decode("ZHlsYW4=") == "dylan"
