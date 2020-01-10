# coding=utf-8
import time
import unittest
from public.common import mytest
from ddt import ddt, data
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case


@ddt
class TestWorkbench(mytest.MyAutologinTest):
    """课程库模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_1_loginout'))
    # @unittest.skipIf(True, "原因")
    def test_1_loginout(self, data):
        """退出登录"""
        test_assert = data['assertion']
        self.workbench.click_get_name()
        loginpage = self.workbench.close()
        text = loginpage.get_title()
        url = loginpage.get_url()
        self.assertIn(test_assert['text'], text)
        self.assertIn(test_assert['url'], url)

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_2'))
    # @unittest.skipIf(True, "原因")
    def test_2(self, data):
        """新建课程"""
        test_assert = data['assertion']
        self.workbench.click_button()
        self.workbench.click_curriculum()
        self.workbench.click_tag()
        self.workbench.input_tag("课程")
        self.workbench.input_name("自动化培训")
        self.workbench.input_student("大学生")
        self.workbench.input_target("完美")
        self.workbench.input_overview("优秀")
        self.workbench.click_determine()
        text = self.workbench.get_kecheng_name()
        url = self.workbench.get_url()
        self.assertIn(text, test_assert['text'])
        self.assertIn(url, test_assert['url'])

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_3'))
    # @unittest.skipIf(True, "原因")
    def test_3(self, data):
        """删除课程"""
        test_assert = data['assertion']
        self.workbench.set_up()
        self.workbench.delete()
        text = self.workbench.get_delete_text()
        url = self.workbench.get_url()
        self.assertIn(test_assert['text'], text)
        self.assertIn(test_assert['url'], url)
        self.workbench.click_out()
        self.workbench.clear_icon()
        self.workbench.set_up()
        self.workbench.forever_delete()
        self.workbench.click_out()

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_4'))
    # @unittest.skipIf(True, "原因")
    def test_4(self, data):
        """点击个人中心"""
        test_assert = data['assertion']
        self.workbench.click_get_name()
        info = self.workbench.personal_center()
        text = info.get_info()
        url = info.get_url()
        self.assertIn(test_assert['text'], text)
        self.assertIn(test_assert['url'], url)