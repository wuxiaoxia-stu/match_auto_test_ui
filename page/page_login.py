# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : page_login
# Time       ：2022/7/14 17:33
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
from selenium.webdriver.common.by import By

from page.page_base import PageBase


class PageLogin(PageBase):
    """登录页元素"""
    # 考试说明 关闭按钮
    login_match_shows_close_x_button_loc = By.XPATH, "//span[@class='ant-modal-close-x']"
    # 账号输入框
    login_username_text_loc = By.XPATH, "//input[@placeholder='请输入用户名']"
    # 密码输入框
    login_password_text_loc = By.XPATH, "//input[@placeholder='请输入密码']"
    # 登录按钮
    login_button_loc = By.XPATH, "//span[text()='登 录']"
    # 登录成功提示
    login_success_alert_loc = By.XPATH, "//span[text()='登录成功']"
    # 退出按钮
    logout_button_loc = By.XPATH, "//span[text()='退出']"
    # 重新开始考试勾选框， 通过弟弟定位哥哥
    restart_exam_checkbox_loc = By.XPATH, "//span[text()='重新开始考试']/preceding-sibling::*"

    """登录页操作"""
    @allure.step('点击考试说明的关闭按钮')
    def click_login_match_shows_close_x_button(self):
        self.base_click(self.login_match_shows_close_x_button_loc)

    @allure.step('输入账号')
    def input_login_username_text(self, username='test'):
        self.base_input(self.login_username_text_loc, username)

    @allure.step('输入密码')
    def input_login_password_text(self, password='666666'):
        self.base_input(self.login_password_text_loc, password)

    @allure.step('点击登录按钮')
    def click_login_button(self):
        self.base_click(self.login_button_loc)

    @allure.step('点击退出按钮')
    def click_logout_button(self):
        self.base_click(self.logout_button_loc)

    @allure.step('勾选重新开始考试')
    def check_restart_exam_checkbox(self):
        self.base_check(self.restart_exam_checkbox_loc)

    # 业务组合
    def login(self, url, username, password):
        self.base_open(url)
        self.base_sleep(2)
        self.base_sleep()
        self.click_login_match_shows_close_x_button()
        self.input_login_username_text(username)
        self.input_login_password_text(password)
        self.click_login_button()

    def login_restart_exam(self, username, password):
        self.click_login_match_shows_close_x_button()
        self.base_sleep()
        self.check_restart_exam_checkbox()
        self.input_login_username_text(username)
        self.input_login_password_text(password)
        self.click_login_button()




