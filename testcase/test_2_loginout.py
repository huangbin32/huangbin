# coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt, data, unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case
from public.pages.LoginPage import Login


@ddt
class TestWorkbench(mytest.MyTest):
    """工作台模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_loginout'))
    def test_loginout(self, data):
        """退出登录"""
        workbench = Login(self.dr).login('18175516432', 'hb123456')
        test_assert = data['assertion']
        workbench.exist_loading()  # 等待全局loading消失
        loginpage = workbench.move_to_element()  # 鼠标悬停右上角名称
        loginpage = workbench.click_out()  # 确认退出
        text = loginpage.get_title()
        url = loginpage.get_url()
        self.assertIn(text, test_assert['text'])  # login.xls里的assertion
        self.assertIn(url, test_assert['url'])
