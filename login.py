from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



def test_login(driver):
    driver.find_element(By.NAME,'username').send_keys("admin")
    driver.find_element(By.NAME,'password').send_keys("admin01")
    driver.find_element(By.XPATH, '//*[@id="loginbox"]/div/div/div/form/div[3]/button').click()
    return driver