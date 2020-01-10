# coding=utf-8
import time
from public.common import basepage
from public.pages import LoginPage
from public.pages.PersonalInfoPage import Info


class WorkBench(basepage.Page):
    """课程库模块"""

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def get_name(self):
        """获取右上角名称"""
        name = self.dr.get_text("css->div.flex.flex--align-center.el-dropdown-selfdefine")
        return name

    def click_get_name(self):
        """点击右上角名称"""
        self.dr.click("css->div.flex.flex--align-center.el-dropdown-selfdefine")
        time.sleep(1)

    def close(self):
        """点击退出按钮"""
        self.dr.click("xpath->//li[contains(text(),'退出')]")
        time.sleep(0.3)

        return LoginPage.Login(self.dr)

    def click_button(self):
        """点击新建按钮"""
        self.dr.click("xpath->//button[@class='el-button el-button--primary el-dropdown-selfdefine']/..")
        time.sleep(1)

    def click_curriculum(self):
        """点击新建课程按钮"""
        self.dr.click("css->ul.creates>li:nth-child(1)")
        time.sleep(1)

    def get_kecheng_name(self):
        """获取创建课程标题"""
        text = self.dr.get_text("css->.course-item__title")
        return text

    def input_name(self, name):
        """输入课程名称"""
        self.dr.clear_type("css->[placeholder='请输入课程名称']", name)

    def click_tag(self):
        """点击课程标签"""
        self.dr.click("css->div.input-tags>button")

    def input_tag(self, tag):
        """输入课程标签"""
        self.dr.clear_type("css->div.input-tags>div>input", tag)

    def input_student(self, student):
        """输入目标学员"""
        self.dr.clear_type("css->[placeholder='请输入目标学员']", student)

    def input_target(self, target):
        """输入学习目标"""
        self.dr.clear_type("css->[placeholder='请输入学习目标']", target)

    def input_overview(self, overview):
        """输入课程综述"""
        self.dr.clear_type("css->[placeholder='请输入课程综述']", overview)

    def click_determine(self):
        """点击确定按钮"""
        self.dr.click("xpath->//span[contains(text(),'确定')]/..")

    def set_up(self):
        """点击设置"""
        self.dr.click("css->span.el-dropdown-link>i")
        time.sleep(3)

    def delete(self):
        """点击删除课程"""
        self.dr.click("css->ul.el-dropdown-menu>li:nth-child(6)")
        time.sleep(0.3)

    def get_delete_text(self):
        """获取确认删除名称"""
        delete_text = self.dr.get_text("css->div.el-message-box__message>p")
        return delete_text

    def click_out(self):
        """确定删除课程"""
        self.dr.click("css->div.el-message-box__btns>button:nth-child(2)")
        time.sleep(2)

    def clear_icon(self):
        """点击删除课程回收站"""
        self.dr.click("css->.icon.mdi.mdi-trash-can-outline")
        time.sleep(1)

    def forever_delete(self):
        """确定永久删除"""
        self.dr.click("css->ul.el-dropdown-menu>li:nth-child(3)")
        time.sleep(1)

    def personal_center(self):
        """点击个人中心"""
        self.dr.click("xpath->//li[contains(text(),'退出')]/../li[1]")
        time.sleep(1)

        return Info(self.dr)

