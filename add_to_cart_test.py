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
    yield
    driver.close()


def test_buttonClick(Setup):
    cart_button = By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]'
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cart_button))
    if button.is_enabled():
        print("Test case pass - Button is clickable")
    else:
        print("Button is not clickable")


def test_productCount(Setup):
    product = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    product.click()
    cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    cart.click()
    count = By.XPATH, '//*[@id="shopping_cart_container"]/a/span'
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(count))
    if cart_count.text == '1':
        print('Product successfully added to the cart!')
    else:
        print('Failed to add the product to the cart.')


def test_multiProduct(Setup):
    product1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    product1.click()
    cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    cart.click()
    driver.back()
    product2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
    product2.click()
    cart1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    cart1.click()
    count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    if count.text > '1':
        print('Two Product successfully added to the cart!')
    else:
        print('Failed to add the two product to the cart.')
        driver.close()


def test_Update_count(Setup):
    product1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    product1.click()
    cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    cart.click()
    driver.back()
    product2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
    product2.click()
    cart1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    cart1.click()
    initial_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    updated_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

    if int(updated_count) == int(initial_count) - 1:
        print('Count change verified successfully.')
    else:
        print('Count change verification failed.')
        driver.close()





