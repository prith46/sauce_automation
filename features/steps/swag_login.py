import time

import allure
from allure_commons.types import AttachmentType
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def get_account_credentials(account_type):
    account = {
        'StandardUser': ("standard_user", "secret_sauce"),
        'LockedOutUser': ("locked_out_user", "secret_sauce")
    }
    return account.get(account_type)


# Scenario 1
@given("I am on the Demo Login Page")
def open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()


@when("I fill the account information for account {account_type} into the Username field and the Password field")
def enter_credentials(context, account_type):
    username, password = get_account_credentials(account_type)
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    allure.attach(context.driver.get_screenshot_as_png(), name="give_credentials", attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when("I click the Login Button")
def click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then("I am redirected to the Demo Main Page")
def check_login(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.url_contains("inventory.html"))
    url = context.driver.current_url
    allure.attach(context.driver.get_screenshot_as_png(), name="success_user_login", attachment_type=AttachmentType.PNG)
    time.sleep(2)
    assert (url == "https://www.saucedemo.com/inventory.html"), "Error in redirecting to Demo Main Page"


@then("I verify the App Logo exists")
def verify_logo(context):
    logo = context.driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed(), "Logo is not displayed in the page"


# Scenario 2
@then('I verify the Error Message contains the text "{error_message}"')
def verify_error(context, error_message):
    text = context.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    allure.attach(context.driver.get_screenshot_as_png(), name="locked_user_login",attachment_type=AttachmentType.PNG)
    time.sleep(2)
    assert (error_message in text), "Provided error message is not displayed"


# Scenario 3
@given("I am on the inventory page")
def login_to_inventory_page(context):
    context.driver.get("https://www.saucedemo.com/")
    username, password = get_account_credentials('StandardUser')
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    allure.attach(context.driver.get_screenshot_as_png(), name="inventory_page",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)
    context.driver.find_element(By.ID, "login-button").click()


@when("user sorts products from high price to low price")
def sorting_products(context):
    element = context.driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(element)
    select.select_by_value("hilo")
    allure.attach(context.driver.get_screenshot_as_png(), name="sorted_page",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when("user adds highest priced product")
def adding_product(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    allure.attach(context.driver.get_screenshot_as_png(), name="adding_product",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when("user clicks on cart")
def click_cart(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    allure.attach(context.driver.get_screenshot_as_png(), name="cart_page",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when("user clicks on checkout")
def click_checkout(context):
    context.driver.find_element(By.ID, "checkout").click()
    allure.attach(context.driver.get_screenshot_as_png(), name="checkout_page",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when("user enters first name {first_name}")
def enter_firstname(context, first_name):
    context.driver.find_element(By.ID, "first-name").send_keys(first_name)


@when("user enters last name {last_name}")
def enter_firstname(context, last_name):
    context.driver.find_element(By.ID, "last-name").send_keys(last_name)


@when("user enters zip code {zip_code}")
def enter_firstname(context, zip_code):
    context.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
    allure.attach(context.driver.get_screenshot_as_png(), name="user_details",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)


@when("user clicks Continue button")
def click_continue(context):
    context.driver.find_element(By.ID, "continue").click()


@then("I verify in Checkout overview page if the total amount for the added item is ${price}")
def check_price(context, price):
    amount = context.driver.find_element(By.CLASS_NAME, "summary_total_label").text
    allure.attach(context.driver.get_screenshot_as_png(), name="checkout_overview",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)
    assert price in amount, "Checkout amount is different"


@when("user clicks Finish button")
def click_finish_button(context):
    context.driver.find_element(By.ID, "finish").click()


@then("Thank You header is shown in Checkout Complete page")
def check_thankyou_message(context):
    text = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    allure.attach(context.driver.get_screenshot_as_png(), name="thankyou_page",
                  attachment_type=AttachmentType.PNG)
    time.sleep(2)
    assert "Thank you for your order!" == text, "Thank you text is missing"
