# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_02_match
# Time       ：2022/7/15 10:14
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure

from cases.base import Base
from page.page_match import PageMatch


@allure.epic('人机大赛系统')
@allure.feature('考试模块')
@allure.severity(allure.severity_level.CRITICAL)
class TestMatch(Base):
    """考试类"""

    @classmethod
    def setup_class(cls):
        cls.page = PageMatch(cls.driver)

    @allure.story('人机大赛考试')
    @allure.title('01用例-暂停测试')
    def test_man_machine_pause_exam(self):
        if self.page.base_element_is_exist(self.page.match_pause_test_button_loc):
            self.page.pause_continue_exam()

    @allure.story('人机大赛考试')
    @allure.title('02用例-答题')
    def test_man_machine_exam(self):
        while not self.page.base_element_is_exist(self.page.match_view_results_button_loc):
            if self.page.base_element_is_exist(self.page.match_switch_button_loc):
                self.page.asynchronous_ai_exam()  # 异步ai
            else:
                self.page.no_asynchronous_ai_exam()  # 非异步ai
        else:
            self.page.base_sleep()
            self.page.click_match_answer_option_no_6()
            self.page.base_sleep()
            self.page.click_match_view_results_button()

    @classmethod
    def teardown_class(cls):
        pass
