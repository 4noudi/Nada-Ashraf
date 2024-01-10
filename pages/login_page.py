from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "user-name")
        self.password_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")
        self.error_message_locator = (By.TAG_NAME, "h3")
        self.logged_in_ttle_locator = (By.CLASS_NAME, "title")

    def enter_username(self, username):
        self.driver.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message_locator)
        )
        return self.driver.find_element(*self.error_message_locator).text
    
    def get_inventory_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        return self.driver.find_element(*self.logged_in_ttle_locator).text
