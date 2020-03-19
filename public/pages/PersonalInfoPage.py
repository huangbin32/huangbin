# coding=utf-8
import time
from public.common import basepage
from public.pages import WorkBenchPage


class Info(basepage.Page):
    """个人信息模块"""

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def get_info(self):
        """获取个人信息名称"""
        text = self.dr.get_text("css->main.el-main>header>h1")
        return text

    def nickname(self):
        """点击昵称修改按钮"""
        self.dr.click("css->ul.list-unstyled.user>li:nth-child(2)>a")

    def get_old_name(self):
        text = self.dr.get_attribute("css->[placeholder='请输入昵称']", "value")
        return text

    def input_username(self, username):
        """修改用户昵称"""
        self.dr.clear_type("css->[placeholder='请输入昵称']", username)

    def username_define(self):
        """点击修改用户昵称确定按钮"""
        self.dr.click("css->div.dialog-form-footer>button:nth-child(2)")
        time.sleep(2)

    def jianjie(self):
        """点击个人简介修改按钮"""
        self.dr.click("css->ul.list-unstyled.user>li:nth-child(3)>a")

    def input_jianjie(self, jianjie):
        """输入个人简介"""
        self.dr.clear_type("css->[placeholder='请输入个人简介']", jianjie)
        time.sleep(0.1)

    def jianjie_define(self):
        """点击个人简介确定按钮"""
        self.dr.click("xpath->//div[@aria-label='个人简介']/div/form/div/button[2]")
        time.sleep(1)

    def kecheng_return(self):
        """点击返回课程库"""
        self.dr.click("css->.el-button")

        return WorkBenchPage.WorkBench(self.dr)
