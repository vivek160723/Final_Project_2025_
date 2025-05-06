import pytest
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config import CONFIG
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.logger import setup_logger

logger = setup_logger("TestSearchMenu")

@pytest.mark.usefixtures("driver")
class TestSearchFunctionality:

    @staticmethod
    def login_to_application(driver):
        logger.info("Navigating to login page")
        driver.get(CONFIG["base_url"])
        login = LoginPage(driver)
        login.login()
        logger.info("Login successful")


    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing valid search: 'Pim'")
        dashboard.search("Pim")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span"))
        )
        assert "pim" in driver.page_source.lower(), "Valid search term did not produce results!"
        logger.info("✅ Valid search successful")




    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing empty search")
        dashboard.search("")


        sidebar_ul_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, sidebar_ul_xpath))
        )

        menu_items = driver.find_elements(By.XPATH, f"{sidebar_ul_xpath}/li")
        assert len(menu_items) > 0, "Expected default menu items on empty search, but found none"
        logger.info("✅ Empty search retained default menu items")



    @allure.severity(allure.severity_level.NORMAL)
    def test_special_character_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing special character search: '!@#$%^&*()'")
        dashboard.search("!@#$%^&*()")

        sidebar_ul_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul"

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, sidebar_ul_xpath))
            )
            menu_items = driver.find_elements(By.XPATH, f"{sidebar_ul_xpath}/li")
            assert len(menu_items) == 0, f"Expected no results, but found {len(menu_items)}"
            logger.info("✅ Special character search returned no results as expected")

        except TimeoutException:
            logger.info("✅ Sidebar menu not present — interpreted as no results for special characters")


    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing invalid search: '@12'")
        dashboard.search("@12")


    @allure.severity(allure.severity_level.NORMAL)
    def test_case_insensitive_search(self, driver):
        self.login_to_application(driver)
        dashboard = DashboardPage(driver)

        logger.info("Performing case-insensitive search: 'PiM'")
        dashboard.search("PiM")
        assert "pim" in driver.page_source.lower(), "Case-insensitive search failed!"
        logger.info("✅ Case-insensitive search successful")