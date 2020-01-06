import unittest, logging
from utils import assert_common

from api.login_api import LoginApi


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

    def test01_login_success(self):
        # 调用封装的登录接口

        response = self.login_api.login('13800000002', '123456')

        # 接收返回的json数据
        jsondata = response.json()

        # 调试输出登录接口返回的数据
        logging.info("登陆成功接口返回的数据为：{}".format(jsondata))

        # # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsondata.get("success"))  # 断言success
        # self.assertEqual(10000, jsondata.get("code"))  # 断言code
        # self.assertIn("操作成功", jsondata.get("message"))  # 断言message

        """调用封装的断言"""
        assert_common(self, response, 200, True, 10000, "操作成功")

    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response = self.login_api.login("13900000002", '123456')

        # 接收返回的json数据
        jsondata = response.json()

        # 调试输出登录接口返回的数据
        logging.info("账号不存在时输出的数据为：{}".format(jsondata))

        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")


    def test03_password_wrong(self):
        # 调用封装的登录接口
        response = self.login_api.login("13800000002", 'error')

        # 接收返回的json数据
        jsondata = response.json()

        # 调试输出登录接口返回的数据
        logging.info("密码错误时输出的数据为：{}".format(jsondata))

        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_username_special_character(self):
        """特殊字符"""
        response = self.login_api.login("138@##$%%%^^",'123456')

        jsondata = response.json()

        logging.info("账号中有特殊字符时输出的数据：{}".format(jsondata))

        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test05_username_is_null(self):
        response = self.login_api.login("",'error')

        jsondata = response.json()

        logging.info("账号中有特殊字符时输出的数据：{}".format(jsondata))

        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test06_password_is_null(self):
        response = self.login_api.login("13800000002", '')

        jsondata = response.json()

        logging.info("账号中有特殊字符时输出的数据：{}".format(jsondata))

        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test07_username_have_chinese(self):
        response = self.login_api.login("1380000平头哥0002", '123456')

        jsondata = response.json()

        logging.info("账号中有特殊字符时输出的数据：{}".format(jsondata))

        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test08_username_have_space(self):
        response = self.login_api.login("1380000 0002", '123456')

        jsondata = response.json()

        logging.info("账号中有特殊字符时输出的数据：{}".format(jsondata))

        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

if __name__ == '__main__':
    unittest.main()
