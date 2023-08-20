import requests

from decorator.retryDecorator import request_retry


class RequestUtil:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get(url, headers=None, expected_status_code=None, attempt=3):
        if headers is None:
            headers = {}

        @request_retry(url=url, method='GET', expected_status_code=expected_status_code, attempt=attempt)
        def request():
            return requests.get(url, headers=headers, verify=False)

        return request

    @staticmethod
    def post(url, headers=None, json=None, expected_status_code=None, attempt=3):
        if json is None:
            json = {}
        if headers is None:
            headers = {}

        @request_retry(url=url, method='POST', expected_status_code=expected_status_code, attempt=attempt)
        def request():
            return requests.post(url, headers=headers, json=json, verify=False)

        return request

    @staticmethod
    def put(url, headers=None, json=None, expected_status_code=None, attempt=3):
        if json is None:
            json = {}
        if headers is None:
            headers = {}

        @request_retry(url=url, method='PUT', expected_status_code=expected_status_code, attempt=attempt)
        def request():
            return requests.put(url, headers=headers, json=json, verify=False)

        return request

    @staticmethod
    def delete(url, headers=None, json=None, expected_status_code=None, attempt=3):
        if json is None:
            json = {}
        if headers is None:
            headers = {}

        @request_retry(url=url, method='DELETE', expected_status_code=expected_status_code, attempt=attempt)
        def request():
            return requests.delete(url, headers=headers, json=json, verify=False)

        return request

    @staticmethod
    def patch():
        pass


if __name__ == "__main__":
    res = RequestUtil.get("https://postman-echo.com/get", "", 200)
    assert (res.status_code == 200)

    try:
        RequestUtil.get("https://postman-echo.com/get", "", 400)
    except Exception as e:
        assert (str(e) == "API请求失败，预期状态码：400，实际状态码：200")

    res = RequestUtil.post("https://postman-echo.com/post", "", {}, 200)
    assert (res.status_code == 200)

    try:
        RequestUtil.post("https://postman-echo.com/post", "", {}, 500)
    except Exception as e:
        assert (str(e) == "API请求失败，预期状态码：500，实际状态码：200")
