# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Kenzhaoyihui
# Date: 2016.11.28

from selenium import webdriver
import time


def LJ():
	dr = webdriver.Firefox()
	id = dr.find_element_by_id
	class_name = dr.find_element_by_class_name
	lj = dr.find_elements_by_class_name
	xpath = dr.find_element_by_xpath

	dr.get("http://180.209.113.96")
	id("txtUserName").send_keys("13030915")
# time.sleep(0.5)
	id("txtPassword").send_keys("13030915")
# time.sleep(0.5)
	id("cmdOK").click()
	time.sleep(2)

	icon = lj("x-tree-ec-icon")
	icon_lj_list = list(icon)
	for i in icon_lj_list[0:3]:
		i.click()
# time.sleep(1)
	time.sleep(1)
	xpath(".//*[@id='ext-gen74']/li[1]/div/a/span").click()
	time.sleep(1)
# dr.switch_to_default_content()
	dr.switch_to_frame("dynamic_added_tabxnode1")
	xpath(".//*[@id='ext-gen45']/div[1]/table/tbody/tr/td[7]/div/a/img").click()
# xpath(".//*[@id='ext-gen45']/div[1]/table/tbody/tr/td[7]/div/a/img").click()
	time.sleep(2)
	dr.switch_to_default_content()
	dr.switch_to_frame("ext-gen98")
	time.sleep(1)
	xpath(".//*[@id='t101001001']").click()
	xpath(".//*[@id='101001001']/div[4]").click()
	time.sleep(1)
	dr.switch_to_frame("ext-gen18")
	id("ext-gen42").click()
	#id("ext-gen41").click()

if __name__ == "__main__":
	LJ()
