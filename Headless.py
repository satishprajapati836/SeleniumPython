from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
driver = webdriver.Chrome(executable_path="/Users/satishprajapati/Downloads/chromedriver",options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
windowopened = driver.window_handles
driver.switch_to.window(windowopened[1])
print(driver.current_url)
driver.close()
driver.switch_to.window(windowopened[0])
print(driver.current_url)
driver.close()