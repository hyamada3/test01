from selenium import webdriver

PROXY = "web-proxy.jp.hpecorp.net:8080"

# Create a copy of desired capabilities object.
desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# Change the proxy properties of that copy.
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

# you have to use remote, otherwise you'll have to code it yourself in python to 
# dynamically changing the system proxy preferences
driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities)


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
