import pytest
import allure
from constants.severity import Severity
from utils.logger import Logger
from utils.time_util import TimeUtil


@allure.feature("登录功能")
class TestLogin:
    def setup_class(self):
        print("\n类级别的钩子，类似 before")

    def teardown_class(self):
        print("\n类级别的钩子，类似 after")

    def setup_method(self):
        print("\n方法级别的钩子，类似 beforeEach")

    def teardown_method(self):
        print("\n方法级别的钩子，类似 afterEach")

    @pytest.mark.P0
    @allure.severity(Severity.BLOCKER.value)
    @allure.title("登录测试-正确的用户名密码")
    @allure.description("登录测试-正确用户名+正确密码")
    @allure.testcase("https://www.baidu.com")
    def test_login_positive(self):
        with allure.step("调用接口进行测试"):
            TimeUtil.sleep(2)
            assert 1 == 1

    @pytest.mark.P1
    @allure.severity(Severity.CRITICAL.value)
    @allure.title("登录测试-正确用户名+错误密码")
    @allure.description("登录测试-正确用户名+错误密码")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_login_right_username_wrong_password(self):
        Logger.info("Test 1234")
        with allure.step("调用接口进行测试"):
            TimeUtil.sleep(2)
            assert 1 != 2

    @pytest.mark.P1
    @allure.severity(Severity.CRITICAL.value)
    @allure.title("登录测试-错误用户名+错误密码")
    @allure.description("登录测试-错误用户名+错误密码")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_login_wrong_username_wrong_password(self):
        with allure.step("调用接口进行测试"):
            TimeUtil.sleep(2)
            assert 1 != 3

    @pytest.mark.P1
    @allure.severity(Severity.CRITICAL.value)
    @allure.title("登录测试-错误用户名+任意正确密码")
    @allure.description("登录测试-错误用户名+任意正确密码")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_login_wrong_username_right_password(self):
        with allure.step("调用接口进行测试"):
            TimeUtil.sleep(2)
            assert 1 != 4
