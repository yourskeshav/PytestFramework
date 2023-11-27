import time
from selenium.webdriver.support.ui import Select
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_testcase1():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    driver.get("https://www.saucedemo.com/")

    userneme_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    userneme_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    title_of_page = driver.find_element(By.XPATH, "//span[@class='title']")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='title']")))

    dropdown_element = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")

    dropdown = Select(dropdown_element)

    dropdown.select_by_value("za")
    time.sleep(5)

    driver.quit()
