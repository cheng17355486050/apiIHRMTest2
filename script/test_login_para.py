import unittest, logging
from utils import assert_common, read_login_data

from api.login_api import LoginApi
from parameterized import parameterized

class TestIHRMLogin(unittest.TestCase):
    def setUp(self) -> None:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    @parameterized.expand(read_login_data)
    def test_login(self,mobile, password, http_code, success, code, message):
        # 调用封装的登录接口

        response = self.login_api.login(mobile, password)

        # 接收返回的json数据
        jsondata = response.json()

        # 调试输出登录接口返回的数据
        logging.info("登陆接口返回的数据为：{}".format(jsondata))

        """调用封装的断言"""
        assert_common(self, response, http_code, success, code, message)