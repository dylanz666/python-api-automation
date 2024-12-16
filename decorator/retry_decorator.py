import functools
import os


def request_retry(**kw):
    def decorate(fun, *args, **kwargs):
        expected_status_code = kw['expected_status_code']
        if expected_status_code is None:
            os.system(f"echo {kw['method']} {kw['url']}")
            return fun(*args, **kwargs)

        status_code = -1
        res = None
        for i in range(kw['attempt']):
            os.system(f"echo Request attempt:{i},{kw['method']} {kw['url']}")
            res = fun(*args, **kwargs)
            status_code = res.status_code
            if status_code == expected_status_code:
                return res
        raise AssertionError(
            f"API请求失败，url：{kw['url']}，预期状态码：{expected_status_code}，实际状态码：{status_code}，返回值：{res.json()}")

    return decorate


def retry(**kw):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            expected_status_code = kw['expected_status_code']
            res = 0
            if expected_status_code is None:
                return fun(*args, **kwargs)

            for i in range(kw['attempt']):
                res = fun(*args, **kwargs)
                print(res, expected_status_code)
                if res == expected_status_code:
                    return res
            os.system(
                f"echo 'API请求失败，预期状态码：{expected_status_code}，实际状态码：{res}'")

        return wrapper

    return decorator


class RetryTest:
    @classmethod
    @retry(expected_status_code=0, attempt=3)
    def test(cls, data):
        print(data)
        return -1


if __name__ == "__main__":
    rer = RetryTest.test(123)
