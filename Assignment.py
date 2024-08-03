import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_opt=Options()
chrome_opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_opt)
driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(2)
driver.get('https://fitpeo.com/revenue-calculator')
time.sleep(2)
driver.execute_script("window.scrollBy(0,400)","")

ele1=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div/span[1]/span[3]')
ActionChains(driver).drag_and_drop_by_offset(ele1,93.8,0).perform()
time.sleep(2)
ele2=driver.find_element(By.ID,(":R57alklff9da:"))
ele2.clear()
time.sleep(2)
ele2.send_keys('560')
driver.execute_script("window.scrollBy(0,40)","")
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[1]/label/span[1]/input').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/label/span[1]/input').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[3]/label/span[2]').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[8]/label/span[1]/input').click()
