#!/usr/bin/env python
#coding=utf-8 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
import time
import traceback
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import httplib2
import re

def login(dd,name,password):
	try:
		ele=dd.find_element_by_xpath("//nav/div[2]/div[12]/a")
		#print len(ele)

		#ele=dd.find_elements_by_class_name("tier0")
		#print type(ele)
		webdriver.ActionChains(dd).move_to_element(ele).perform()

	except:
		print "move to login failed"
		print traceback.print_exc()

	#time.sleep(0.5)


	try:
		ele = dd.find_element_by_xpath("//form[@name = 'login-form']//input[@id = 'exp-login-email']")
		ele.clear()
		ele.send_keys(name)

	except:
		print 'input name failed'
		print traceback.print_exc()


	try:
		ele = dd.find_element_by_xpath("//form[@name = 'login-form']//input[@id='exp-login-password']")
		ele.clear()
		ele.send_keys(password)
	except:
		print 'input password failed'
		print traceback.print_exc()


	#time.sleep(0.5)

	try:
		ele = dd.find_element_by_xpath("//form[@name='login-form']//button[@type='submit']")
		ele.click()

	except:
		print 'login submit failed'
		print traceback.print_exc()


def find_new(tpe):
	#provide the address
	h=httplib2.Http()
	resp, content = h.request("http://store.nike.com/cn/zh_cn/pw/%E7%94%B7%E5%AD%90-jordan-%E9%9E%8B%E7%B1%BB/7puZbrkZc8d") 
	print resp.fromcache
	m=re.findall(r'<a href=\"(http://store\.nike\.com/cn/zh_cn/pd/air-jordan.*-%d-.+)\">'%tpe,content)
	if m:
		return m[0]




def book(dd,url,size):
	#dd.set_page_load_timeout(15)
	try:
		dd.get(url)
	except :
		print traceback.print_exc()

	try:
		ele1=dd.find_element_by_xpath("//div[@id='exp-pdp-buying-tools-container']/form/div[1]/div[1]/a")
		ele1.click()
		ele2=dd.find_elements_by_xpath("//div[@id='exp-pdp-buying-tools-container']/form/div[1]/div[1]/div/ul/li")
		for e in ele2:
			s=e.text[3:]
			s=s.strip()
			if str(size) == s:
				e.click()
				break
		#ele2.click()
	except:
		print "size choose failed"
		print traceback.print_exc()


	try:
		ele=dd.find_element_by_xpath("//div[@id='exp-pdp-buying-tools-container']/form/div[2]/button")
		ele.click()

	except:
		print "click failed"
		print traceback.print_exc()




#dd= webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
#dd = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS) 
dd= webdriver.Firefox()
dd.maximize_window()
dd.implicitly_wait(1)
dd.get("http://store.nike.com/cn/zh_cn/pw/Jordan-%E9%9E%8B%E7%B1%BB/brkZc8d")
print '!!!!'
login(dd,'xxxxxxxx@qq.com','xxxxxx')
time.sleep(10)
url = find_new(2)
while not url:
	find_new(2)
print 'find url'
book(dd,url,42.5)

