import app
import logging

# 初始化日志器
# 为什么要在api.init.py中初始化日志呢？
# 这是因为，我们后面进行接口测试时，都会调用封装的API接口，调用时，会自动运行__init__.py函数，初始化日志器
# 从而实现，自动化初始日志的功能
app.init_logging()

logging.info("TEST日志器能不能正常工作")