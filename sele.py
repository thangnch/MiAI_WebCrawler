from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
#option.add_argument('headless')
driver = webdriver.Chrome('./chromedriver',options=option)

print("sample test case started")
#driver = webdriver.Chrome(options=)
#driver=webdriver.firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.aivivn.com/")
time.sleep(3)
#click on the Google search button
button = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/button")
button.click()
time.sleep(20)
#Number = driver.find_element_by_xpath("/html/body/div[20]/div/div[1]/div/div[1]/div[3]/div[2]/ul/li[1]/div[1]").text
#print("Số người nhiễm: ", Number)
#print(driver.find_element_by_class_name("statistic_number red"))
#close the browser
#driver.close()
#print("sample test case successfully completed")