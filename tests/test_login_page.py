import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CONFIG
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger('TestLogin')


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(driver):
    logger.info("Navigating to login page")
    driver.get(CONFIG["base_url"])

    login_page = LoginPage(driver)
    logger.info("Entering valid credentials")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_btn()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    assert "dashboard" in driver.current_url.lower()
    logger.info("Login Successful")


@pytest.mark.negative
@pytest.mark.regression
def test_empty_username(driver):
    logger.info("Navigating to login page")
    driver.get(CONFIG["base_url"])

    login_page = LoginPage(driver)
    logger.info("Entering empty username")
    login_page.enter_username("")
    login_page.enter_password("admin123")
    login_page.click_login_btn()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span"))
    )
    error_text = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
    assert "Required" in error_text
    logger.warning("Login failed as expected with empty username")

@pytest.mark.negative
@pytest.mark.regression
def test_empty_password(driver):
    logger.info("Navigating to login page")
    driver.get(CONFIG["base_url"])

    login_page = LoginPage(driver)
    logger.info("Entering empty password")
    login_page.enter_username("Admin")
    login_page.enter_password("")
    login_page.click_login_btn()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span"))
    )
    error_text = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text
    assert "Required" in error_text
    logger.warning("Login failed as expected with empty password")

@pytest.mark.negative
@pytest.mark.regression
def test_password_only(driver):
    logger.info("Navigating to login page")
    driver.get(CONFIG["base_url"])

    login_page = LoginPage(driver)
    logger.info("Entering only password")
    login_page.enter_username("")
    login_page.enter_password("admin123")
    login_page.click_login_btn()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span"))
    )
    error_text = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
    assert "Required" in error_text
    logger.warning("Login failed as expected with password but no username")