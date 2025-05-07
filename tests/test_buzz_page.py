import pytest
from config import CONFIG
from pages.login_page import LoginPage
from pages.buzz_page import BuzzPage
from utils.logger import setup_logger

logger = setup_logger("BuzzTest")

@pytest.mark.usefixtures("driver_setup")
class TestBuzz:

    def test_post_buzz_message(self):
        self.driver.get(CONFIG["base_url"])
        login = LoginPage(self.driver)
        buzz = BuzzPage(self.driver)

        logger.info("Logging in as Admin")
        login.login("Admin", "admin123")

        logger.info("Navigating to Buzz module")
        buzz.go_to_buzz()

        message = "Hello, Buzz!"
        logger.info(f"Posting message: {message}")
        buzz.enter_buzz_post(message)
        buzz.click_post_button()

        logger.info("Verifying that message is posted")
        assert buzz.is_post_successful(message), f"Message '{message}' not found in the Buzz feed"