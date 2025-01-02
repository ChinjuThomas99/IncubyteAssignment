from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_sign_up(driver):
    driver.find_element(By.LINK_TEXT,"Create an Account").click()
    WebDriverWait(driver,20)
            
    driver.find_element(By.ID,"firstname").send_keys("Test")
    driver.find_element(By.ID,"lastname").send_keys("User")
    driver.find_element(By.XPATH,"//*[@id='email_address']").send_keys("testuser37889@yahoo.com")
    driver.find_element(By.XPATH,"//*[@id='password']").send_keys("testuser@37889")
    driver.find_element(By.XPATH,"//*[@id='password-confirmation']").send_keys("testuser@37889")
    driver.find_element(By.XPATH,"//*[@id='form-validate']/div/div[1]/button/span").click()
        
    WebDriverWait(driver,20)
    element = driver.find_element(By.XPATH,"//*[@id='maincontent']/div[1]/div[2]/div/div/div")
    actual_text = element.text
        
    expected_text = "Thank you for registering with Main Website Store."
        
    assert actual_text == expected_text, f"Assertion failed:Expected '{expected_text}',but got '{actual_text}'."
    print("Assertion Passed: Account Created")

            
        