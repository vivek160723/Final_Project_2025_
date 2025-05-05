import pytest
import allure

from config import config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.logger import setup_logger

logger = setup_logger("TestSearchMenu")

@pytest.mark.usefixtures("driver")
class TestSearchFunctionality:

    def login_to_application(self, driver):
        logger.info("Navigating to login page")
        driver.get(config.BASE_URL)
        login = LoginPage(driver)
        login.login()
        logger.info("Login successful")

    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing valid search: 'Pim'")
        dashboard.search("Pim")
        assert "pim" in driver.page_source.lower(), "Valid search term did not produce results!"
        logger.info("✅ Valid search successful")

    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing invalid search: '@12'")
        dashboard.search("@12")

        assert "dashboard" in driver.current_url.lower(), "Empty search caused unexpected behavior!"
        logger.info("✅ Empty search handled correctly")

    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing empty search")
        dashboard.search("")
        assert "dashboard" in driver.current_url.lower(), "Empty search caused unexpected behavior!"
        logger.info("✅ Empty search handled correctly")

    @allure.severity(allure.severity_level.NORMAL)
    def test_special_character_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing special character search: '!@#$%^&*()'")
        dashboard.search("!@#$%^&*()")
        assert "no records found" in driver.page_source.lower(), "Special character search caused unexpected results!"
        logger.info("✅ Special character search handled correctly")

    @allure.severity(allure.severity_level.NORMAL)
    def test_case_insensitive_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing case-insensitive search: 'PiM'")
        dashboard.search("PiM")
        assert "pim" in driver.page_source.lower(), "Case-insensitive search failed!"
        logger.info("✅ Case-insensitive search successful")