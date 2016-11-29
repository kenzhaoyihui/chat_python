# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Kenzhaoyihui
# Date: 2016.11.29
# Email: kenzhaoyihui@gmail.com
"""
from splinter import Browser

with Browser() as browser:
	# Visit URL
	url = "http://www.google.com"
	browser.visit(url)
	browser.fill('q', 'splinter - python acceptance testing for web application')
	# Find and click the 'search' button
	button = browser.find_by_name('btnG')
	button.click()
	print(browser.is_text_present)
	b
	if browser.is_text_present('splinter.readthedocs.io'):
		print("Yes, the offical website was found!")
	else:
		print("No, it wasn't found... We need to improve our SEO techniques")
"""

from splinter import Browser
import time


username = "13030915"
password = "13030915"
url = "http://180.209.113.96"
init_url = "http://180.209.113.96/Florms/FormSYS.aspx"


def login():
	b.fill("txtUserName", username)
	b.fill("txtPassword", password)
	b.find_by_id("cmdOK").click()


def lj():
	global b
	b = Browser(driver_name='firefox')
	b.visit(url)
	b.execute_script('alert("Begin input!~~~")')
	time.sleep(1)
	b.get_alert().dismiss()

	while b.is_element_present_by_id("cmdOK"):
		login()
		if b.url == init_url:
			break
	b.find_by_text(u"展开全部").click()
	time.sleep(1)
	b.find_by_xpath(".//*[@id='ext-gen74']/li[1]/div/a/span").click()
	b.driver.switch_to_frame("dynamic_added_tabxnode1")
	while b.is_element_not_present_by_xpath(".//*[@id='ext-gen45']/div[2]/table/tbody/tr/td[7]/div/a/img"):
		time.sleep(2)
		continue
	b.find_by_xpath(".//*[@id='ext-gen45']/div[3]/table/tbody/tr/td[7]/div/a/img").click()

	b.driver.switch_to_default_content()
	b.driver.switch_to_frame("ext-gen107")
	while b.is_element_not_present_by_xpath(".//*[@id='t101003015']"):
		time.sleep(2)
		continue
	b.find_by_xpath(".//*[@id='t101003015']").click()

	b.find_by_xpath(".//*[@id='101003015']/div[4]").click()
	b.driver.switch_to_frame("ext-gen18")
	while b.is_element_not_present_by_text(u"重新选择"):
		time.sleep(2)
		continue
	b.find_by_text(u"重新选择").click()






if __name__ == "__main__":
	lj()