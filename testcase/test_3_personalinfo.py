# coding=utf-8
import time
import unittest
from public.common import mytest
from ddt import ddt, data
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case


@ddt
class Personalinfo(mytest.MyuserloginTest):
    """个人信息模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_1_info'))
    # @unittest.skipIf(True, "原因")
    def test_1_info(self, data):
        """修改个人信息"""
        test_assert = data['assertion']
        self.user.nickname()
        self.user.input_username("HB")
        self.user.username_define()
        self.user.jianjie()
        self.user.input_jianjie("本人性格热情开朗")
        self.user.jianjie_define()
        WorkBench = self.user.kecheng_return()
        username = WorkBench.get_name()
        url = WorkBench.get_url()
        self.assertIn(test_assert['username'], username)
        self.assertIn(test_assert['url'], url)
