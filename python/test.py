from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.jd.com")

driver.find_element("id", "key").send_keys("手机")
driver.find_element("id", "key").send_keys(Keys.ENTER)
driver.get("https://www.jd.com")
driver.find_element('id', 'key').clear()
driver.find_element("id", "key").send_keys("电脑")
driver.find_element("id", "key").send_keys(Keys.ENTER)

