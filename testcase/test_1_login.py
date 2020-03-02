# coding=utf-8
import time
from public.common import mytest
from public.pages import LoginPage
from ddt import ddt, data
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case


@ddt
class TestLogin(mytest.MyTest):
    """登录模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_01_login'))
    # @unittest.skipIf(True, "原因")
    def test_01_login(self, data):
        """正常登录"""
        test_data = data['data']
        test_assert = data['assertion']
        login = LoginPage.Login(self.dr)
        ele = login.login(test_data['username'], test_data['pw'])
        username = ele.get_name()
        url = ele.get_url()
        self.assertIn(test_assert['username'], username)
        self.assertIn(test_assert['url'], url)

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_02_login'))
    # @unittest.skipIf(True, "原因")
    def test_02_login(self, data):
        """密码错误登录"""
        test_data = data['data']
        test_assert = data['assertion']
        login = LoginPage.Login(self.dr)
        ele = login.login(test_data['username'], test_data['pw'])
        error_text = login.get_error_text()
        url = ele.get_url()
        self.assertIn(test_assert['error_text'], error_text)
        self.assertIn(test_assert['url'], url)

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_03_login'))
    def test_03_login(self, data):
        """用户名不存在"""
        test_data = data['data']
        test_assert = data['assertion']
        login = LoginPage.Login(self.dr)
        ele = login.login(test_data['username'], test_data['pw'])
        error_text = login.get_error_text()
        url = ele.get_url()
        self.assertIn(test_assert['error_text'], error_text)
        self.assertIn(test_assert['url'], url)