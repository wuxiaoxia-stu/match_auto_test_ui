# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : page_match
# Time       ：2022/7/14 18:19
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
from selenium.webdriver.common.by import By

from page.page_base import PageBase


class PageMatch(PageBase):
    """考试页元素"""
    # 答案选项
    def match_answer_options_button_loc(self):
        return self.driver.find_elements(By.XPATH, "//label[@class='ant-radio-wrapper']")

    # 切换对比图按钮
    match_switch_button_loc = By.XPATH, "//span[text()='切换对比图']"
    # 下一题按钮
    match_next_button_loc = By.XPATH, "//span[text()='下一题']"
    # 暂停测试按钮
    match_pause_test_button_loc = By.XPATH, "//span[text()='暂停测试']"
    # 继续测试按钮
    match_continue_test_button_loc = By.XPATH, "//span[text()='继续测试']"
    # 查看成绩按钮
    match_view_results_button_loc = By.XPATH, "//span[text()='查看成绩']"

    """页面操作"""
    @allure.step('点击13个答案')
    def click_match_answer_options_button(self):
        for answer in self.match_answer_options_button_loc():
            self.base_click(answer)

    @allure.step('点击答案选项6')
    def click_match_answer_option_no_6(self):
        # print(self.match_answer_options_button_loc())
        # print(self.match_answer_options_button_loc()[5])
        self.match_answer_options_button_loc()[5].click()

    @allure.step('点击切换对比图按钮')
    def click_match_switch_button(self):
        self.base_click(self.match_switch_button_loc)

    @allure.step('点击下一题按钮')
    def click_match_next_button(self):
        self.base_click(self.match_next_button_loc)

    @allure.step('点击暂停测试按钮')
    def click_match_pause_test_button(self):
        self.base_click(self.match_pause_test_button_loc)

    @allure.step('点击继续测试按钮')
    def click_match_continue_test_button(self):
        self.base_click(self.match_continue_test_button_loc)

    @allure.step('点击查看成绩按钮')
    def click_match_view_results_button(self):
        self.base_click(self.match_view_results_button_loc)

    @allure.step('非异步AI辅助题型考试')
    def no_asynchronous_ai_exam(self):
        self.click_match_answer_option_no_6()
        if self.base_element_is_exist(self.match_next_button_loc):
            self.click_match_next_button()
        if self.base_element_is_exist(self.match_view_results_button_loc):
            self.click_match_view_results_button()

    @allure.step('异步AI辅助题型考试')
    def asynchronous_ai_exam(self):
        self.click_match_answer_option_no_6()
        self.click_match_switch_button()
        self.click_match_answer_option_no_6()
        if self.base_element_is_exist(self.match_next_button_loc):
            self.click_match_next_button()
        if self.base_element_is_exist(self.match_view_results_button_loc):
            self.click_match_view_results_button()

    @allure.step('暂停/继续考试')
    def pause_continue_exam(self):
        self.click_match_pause_test_button()
        self.base_sleep(2)
        self.click_match_continue_test_button()












