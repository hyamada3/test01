from selenium import webdriver 
from selenium.webdriver import DesiredCapabilities 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

option = Options()
PROXY = 'web-proxy.jp.hpecorp.net:8080'
option.add_argument('--proxy-server=http://%s' % PROXY)

driver = webdriver.Remote(
command_executor='http://0.0.0.0:4444/wd/hub',
desired_capabilities={
    'browserName': 'chrome',
    'chromeOptions': {
       'args': [
           '--start-maximized',
           '--proxy-server=http://web-proxy.jp.hpecorp.net:8080'
               ]
     }
 })

driver.get("http://www.yahoo.co.jp")
driver.save_screenshot("/home/hyamada/selenium/screenshot/screen01.png")
print (driver.title)

elem_search_word = driver.find_element_by_id("srchtxt")
elem_search_word.send_keys("selenium")
elem_search_btn = driver.find_element_by_id("srchbtn")
elem_search_btn.click()
 
print (driver.title)
elements_a = driver.find_elements_by_css_selector("#WS2m .w .hd h3 a") 
for elem in elements_a:
       url = elem.get_property("href")
       print(url)

driver.get("http://www.python.org")
driver.save_screenshot("/home/hyamada/selenium/screenshot/screen02.png")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.get("http://www.google.com")
driver.save_screenshot("/home/hyamada/selenium/screenshot/screen03.png")
print (driver.title)

driver.back()
driver.forward()

#driver.get_log("client")

#print (driver.page_source)

#driver.get_screenshot_as_file(/home/hyamada/selenium/log/Screenshots/foo.png)
#driver.get_screenshot_as_png()

#driver.maximize_window()
driver.close()
#driver.quit()


