import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


def valid_login(username, password):
    driver.get('https://www.saucedemo.com/')
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    button = driver.find_element(By.ID, 'login-button')
    print(button.is_enabled())
    button.click()
    time.sleep(3)

    if driver.title == 'Swag Labs':
        print("login successfully-test case pass")
    else:
        print(" login test failed")


def invalid_user_login(username, password):
    driver.get('https://www.saucedemo.com/')
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    driver.find_element(By.ID, 'login-button').click()
    time.sleep(3)

    err_msg = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    if err_msg.is_displayed():
        print("Test case passed: Invalid username and valid password")
    else:
        print("Test case failed: Invalid username and valid password")


def invalid_pass_login(username, password):
    driver.get('https://www.saucedemo.com/')
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    driver.find_element(By.ID, 'login-button').click()
    time.sleep(3)

    err_msg = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    if err_msg.is_displayed():
        print("Test case passed: valid username and Invalid password")
    else:
        print("Test case failed: valid username and Invalid password")


def invalid_user_pass_login(username, password):
    driver.get('https://www.saucedemo.com/')
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    driver.find_element(By.ID, 'login-button').click()
    time.sleep(3)

    err_msg = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    if err_msg.is_displayed():
        print("Test case passed: Invalid username and Invalid password")
    else:
        print("Test case failed: Invalid username and Invalid password")


def blank_user_login(username, password):
    driver.get('https://www.saucedemo.com/')
    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    driver.find_element(By.ID, 'login-button').click()
    time.sleep(3)

    err_msg = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    if err_msg.is_displayed():
        print("Test case passed: Blank username and Blank password")
    else:
        print("Test case failed: Blank username and Blank password")


valid_login('standard_user', 'secret_sauce')
invalid_user_login('cool_user', 'secret_sauce')
invalid_pass_login('standard_user', 'one_man_army')
invalid_user_pass_login('sweet_user', 'doremon@123')
blank_user_login('', '')

driver.quit()
