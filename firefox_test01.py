from selenium import webdriver
from selenium.webdriver.common.proxy import *

myProxy = "web-proxy.jp.hpecorp.net:8080"

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })

# driver = webdriver.Firefox(proxy=proxy)

# for remote
caps = webdriver.DesiredCapabilities.FIREFOX.copy()
proxy.add_to_capabilities(caps)

driver = webdriver.Remote("http://localhost:4443/wd/hub", desired_capabilities=caps)

driver.get("http://www.yahoo.co.jp")
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

