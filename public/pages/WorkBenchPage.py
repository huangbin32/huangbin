# coding=utf-8
import time
from public.common import basepage
from public.pages import LoginPage


class WorkBench(basepage.Page):
    """退出登录模块"""

    def get_name(self):
        """获取右上角名称"""
        name = self.dr.get_text("class->user-name")
        return name

    def move_to_element(self):
        """鼠标悬停右上角名称"""
        self.dr.move_to_element("xpath->//span[@class='el-avatar el-avatar--circle']/..")

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def close(self):
        """关闭按钮"""
        self.dr.click("class->close")
        time.sleep(0.3)

    def click_out(self):
        """确定退出"""
        self.dr.click("xpath->//li[contains(text(),'退出')]")

        return LoginPage.Login(self.dr)
