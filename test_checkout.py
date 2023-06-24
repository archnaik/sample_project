import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = None


@pytest.fixture()
def Setup():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    yield
    driver.close()


def test_checkout(Setup):
    checkout_input = By.XPATH, '//*[@id="checkout"]'
    button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(checkout_input))
    if button.is_enabled():
        print("Test case pass - checkout_Button is clickable")
    else:
        print("checkout_Button is not clickable")
        driver.close()


def test_Cancel(Setup):
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    cancel_input = By.ID, 'cancel'
    cancel_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cancel_input))
    if cancel_button.is_enabled:
        print('test case pass- cancel button clickable')
    else:
        print('test case failed - cancel button not clickable')
        driver.close()


def test_Continue(Setup):
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('archana')
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys('more')
    zip_code = driver.find_element(By.ID, 'postal-code')
    zip_code.send_keys('414105')
    cont_input = driver.find_element(By.ID, 'continue')
    cont_input.click()

    title = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    if title.text == 'Checkout: Overview':
        print('test case pass')
    else:
        print('test case fail')


def test_blankDetails(Setup):
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('')
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys('')
    zip_code = driver.find_element(By.ID, 'postal-code')
    zip_code.send_keys('')
    cont_input = driver.find_element(By.ID, 'continue')
    cont_input.click()
    err_msg = driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')
    if err_msg.is_displayed():
        print('test case passed - blank details')
    else:
        print('test case fail - blank details')























