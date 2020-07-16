# coding=utf-8
import time
import unittest
from public.common import mytest
from ddt import ddt, data
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case


@ddt
class TestMaterial(mytest.MaterialloginTest):
    """素材库模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_1_material'))
    # @unittest.skipIf(True, "原因")
    def test_1_material(self, data):
        """个人智慧空间"""
        test_assert = data['assertion']
        self.material.click_folder()
        self.material.input_foldername("素材")
        self.material.confirm_foldername()
        text = self.material.get_foldername()
        url = self.material.get_url()
        self.assertIn(text, test_assert['text'])
        self.assertIn(url, test_assert['url'])
        self.material.delete_icon()
        self.material.click_icon()
        self.material.secondary_confirmation()
        result = self.material.is_sucai()
        self.assertFalse(result)  #检查表达式是否为假

