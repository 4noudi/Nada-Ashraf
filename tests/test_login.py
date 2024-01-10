import unittest
from parameterized import parameterized
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
import sys
import os
from test_base import TestBase

### don't worry about, it's just letting the python kernel where the root folder is
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
from pages.login_page import LoginPage

# configure logging
logger = logging.getLogger(__name__)


class TestLogin(TestBase):
    ### ################ TEST CASES ############### ###
    ### ("username", "password", "error if applicable")
    users_to_test = [
        ("standard_user", "secret_sauce"),                                                                                  ## login normally expected
        ("problem_user", "secret_sauce"),                                                                                   ## login normally expected
        ("performance_glitch_user", "secret_sauce"),                                                                        ## login normally expected
        ("error_user", "secret_sauce"),                                                                                     ## login normally expected
        ("visual_user", "secret_sauce"),                                                                                    ## login normally expected
        ("standard_user", "wrong_password", 'Epic sadface: Username and password do not match any user in this service'),   ## error login expected
        ("invalid_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),    ## error login expected
        ("wrong_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),        ## error login expected
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),                         ## error login expected    
        ("", "", "Epic sadface: Username is required"),                                                                     ## error login expected
        ("", "secred_sauce", "Epic sadface: Username is required"),                                                         ## error login expected
        ("standard_user", "", "Epic sadface: Password is required")                                                         ## error login expected
    ]

    # Use the parameterized decorator to pass a list of usernames and passwords
    @parameterized.expand(users_to_test)
    def test_login(self, username, password, error=None):
        logger.info(f'Testing user: {username}')
        
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()

        if error is None:
            inventory_title = login_page.get_inventory_title()
            self.assertEqual(inventory_title, "Products")
            logger.info('## Normal login PASS ##')
        else:
            actual_error = login_page.get_error_message()
            self.assertEqual(actual_error, error)
            logger.info('## Login inacceptance PASS ##')
