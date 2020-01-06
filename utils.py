import json

import pymysql

from app import BASE_DIR


def assert_common(self, response, http_code, success, code, message):
    # 断言
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言message


def read_login_data():
    data_path = BASE_DIR + "/data/login_data.json"
    with open(data_path, 'r', encoding='utf-8') as f:
        # 加载文件为json格式的数据
        jsondata = json.load(f)

        p_list = []
        # 遍历文件取出其中数据并保存在列表中
        for data in jsondata:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append((
                mobile, password, http_code, success, code, message
            ))

        print(p_list)
        return p_list


def read_add_emp():
    path = BASE_DIR + "/data/employee.json"

    # 打开文件
    with open(path, "r", encoding="utf-8") as f:
        jsondata = json.load(f)

        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取其中的值
        add_emp_data = jsondata.get("add_emp")
        result_list = []

        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        http_code = add_emp_data.get("http_code")
        result_list.append((username, mobile, success, code, message, http_code))

    print("添加员工的数据", result_list)
    return result_list


def read_query_emp_data():
    path = BASE_DIR + "/data/employee.json"

    # 打开文件
    with open(path, "r", encoding="utf-8") as f:
        jsondata = json.load(f)

        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取其中的值
        query_emp_data = jsondata.get("query_emp")
        result_list = []

        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        http_code = query_emp_data.get("http_code")
        result_list.append((success, code, message, http_code))

    print("查看员工的数据", result_list)
    return result_list


def read_modify_emp_data():
    path = BASE_DIR + "/data/employee.json"

    # 打开文件
    with open(path, "r", encoding="utf-8") as f:
        jsondata = json.load(f)

        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取其中的值
        modify_emp_data = jsondata.get("modify_emp")
        result_list = []
        username = modify_emp_data.get("username")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        http_code = modify_emp_data.get("http_code")
        result_list.append((username,success, code, message, http_code))

    print("修改员工的数据", result_list)
    return result_list

def read_delete_emp_data():
    path = BASE_DIR + "/data/employee.json"

    # 打开文件
    with open(path, "r", encoding="utf-8") as f:
        jsondata = json.load(f)

        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取其中的值
        delete_emp_data = jsondata.get("delete_emp")
        result_list = []
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        http_code = delete_emp_data.get("http_code")
        result_list.append((success, code, message, http_code))

    print("删除员工的数据", result_list)
    return result_list

class DBUtils:
    def __init__(self,host='182.92.81.159',user='readuser',password='iHRM_user_2019',database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        self.conn = pymysql.connect(self.host,self.user,self.password,self.database)
        self.cursor = self.conn.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    # main函数的作用
    # 防止调用这个模块或者类时，自动执行代码
    # read_login_data()
    with DBUtils() as db_utils:
        db_utils.execute("select * from bs_user limit 1")
        print(db_utils.fetchone())