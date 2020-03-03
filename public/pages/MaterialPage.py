# coding=utf-8
import time
from public.common import basepage


class Material(basepage.Page):
    """素材库模块"""

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def get_video_text(self):
        """获取视频文字"""
        name = self.dr.get_text("xpath->//span[text()='视频']")
        return name

    def click_folder(self):
        """点击添加文件夹"""
        self.dr.click("css->li.category-item")

    def input_foldername(self, name):
        """输入文件夹名称"""
        self.dr.clear_type("css->[placeholder='请输入文件夹名称']", name)

    def confirm_foldername(self):
        """点击确定"""
        self.dr.click("css->div.dialog-form-footer>button:nth-child(2)")
        time.sleep(1)

    def get_foldername(self):
        """获取输入的文件夹名称"""
        text = self.dr.get_text("css->.text-ellipsis")
        return text
