# coding=utf-8

import unittest
from public.common import pyselenium
from config import globalparam
from config.basic_config import ConfigInit
from loguru import logger
from public.pages.LoginPage import Login


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """

    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser, globalparam.headless)
        self.dr.max_window()
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))

    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')


class MyAutologinTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     MongoModel().delete_customer('13800138011')

    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser, globalparam.headless)
        self.dr.max_window()
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))
        self.workbench = Login(self.dr).login('c', 'hb123456')

    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')


class MyuserloginTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     MongoModel().delete_customer('13800138011')

    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser, globalparam.headless)
        self.dr.max_window()
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))
        self.workbench = Login(self.dr).login('18175516432', 'hb123456')
        self.workbench.click_get_name()
        self.user = self.workbench.personal_center()

    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')


class MaterialloginTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethodm
    # def tearDownClass(cls):
    #     MongoModel().delete_customer('13800138011')

    def setUp(self):
        logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser, globalparam.headless)
        self.dr.max_window()
        self.dr.open(ConfigInit.url)
        logger.info('打开{}'.format(ConfigInit.url))
        self.workbench = Login(self.dr).login('18175516432', 'hb123456')
        self.material = self.workbench.personal_wisdomspace()

    def tearDown(self):
        self.dr.quit()
        logger.info('###############################  End  ###############################')
