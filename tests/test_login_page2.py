import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CONFIG
from pages.login_page import LoginPage
from utils.db_utils import get_test_data_from_db
from utils.logger import setup_logger


logger = setup_logger('TestLogin')


# Update the get_test_data_from_db() to return only the username and password
@pytest.mark.parametrize("username,password", get_test_data_from_db())
@pytest.mark.regression
def test_login_ddt(driver, username, password):
    logger.info(f"Testing login with: username='{username}' password='{password}'")
    driver.get(CONFIG["base_url"])

    login_page = LoginPage(driver)
    login_page.enter_username("" if username == "(empty)" else username)
    login_page.enter_password("" if password == "(empty)" else password)
    login_page.click_login_btn()

    wait = WebDriverWait(driver, 10)

    # Conditional expected outcome based on the input credentials
    if username == "Admin" and password == "admin123":
        expected = "success"
    elif not username:
        expected = "username_required"
    elif not password:
        expected = "password_required"
    else:
        expected = "invalid_credentials"

    # Handle different expected outcomes
    if expected == "success":
        wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        assert "dashboard" in driver.current_url.lower()
        logger.info("Login successful")

    elif expected == "invalid_credentials":
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")))
        error = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        assert "Invalid credentials" in error
        logger.warning("Login failed as expected: Invalid credentials")

    elif expected == "username_required":
        wait.until(EC.visibility_of_element_located((By.XPATH, "//form/div[1]/div/span")))
        error = driver.find_element(By.XPATH, "//form/div[1]/div/span").text
        assert "Required" in error
        logger.warning("Login failed as expected: Username required")

    elif expected == "password_required":
        wait.until(EC.visibility_of_element_located((By.XPATH, "//form/div[2]/div/span")))
        error = driver.find_element(By.XPATH, "//form/div[2]/div/span").text
        assert "Required" in error
        logger.warning("Login failed as expected: Password required")
