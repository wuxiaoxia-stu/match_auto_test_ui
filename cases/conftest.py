from util.yaml_util import YamlUtil
import pytest


@pytest.fixture(name="login_data")
def get_login_data():
    """获取url，登录账号和密码"""
    data_login = YamlUtil.read_yaml('login.yaml')['login']  # 读取登录的配置文件
    yield data_login
    # print(data_login)
