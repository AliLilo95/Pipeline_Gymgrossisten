from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait


# Setup and Teardown for each test
@pytest.fixture
def load_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Tester>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

# Test 1
def test_01(load_driver):
    
    driver = load_driver
    driver.get("https://www.gymgrossisten.com/")
    far = driver.find_element(By.XPATH, "/html/body/div[3]/header/div[1]/div/div[2]/div[1]/div/ul/li[3]/span/span")
    assert(far.text, "Prisgaranti")