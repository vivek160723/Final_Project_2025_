import pytest

from config import CONFIG
from pages.recruitment import Recruit
from pages.login_page import LoginPage
from utils.logger import setup_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logger
logger = setup_logger("RecruitTest")

@pytest.mark.usefixtures("driver_setup")
class TestRecruitment:

    def test_add_recruitment_entry(self):
        self.driver.get(CONFIG["base_url"])
        login = LoginPage(self.driver)
        recruit = Recruit(self.driver)

        logger.info(" Logging in as Admin")
        login.login("Admin", "admin123")  # ✅ Reusing existing LoginPage POM

        logger.info(" Login successful. Waiting for Recruitment tab to be visible.")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(recruit.recruitementbutton)
        )

        logger.info(" Navigating to Recruitment module")
        recruit.click_recruitment()

        logger.info(" Waiting for Add button")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(recruit.addbutton)
        )
        recruit.click_add_button()

        logger.info("✍ Filling candidate details")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(recruit.firstname)
        )
        recruit.enter_first_name("John")
        recruit.enter_last_name("Doe")
        recruit.enter_email("john.doe@example.com")

        logger.info(" Selecting Job Vacancy")
        recruit.select_job_vacancy()

        logger.info("Saving recruitment entry")
        recruit.click_save_button()

        logger.info(" Verifying success message")
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(recruit.successmessage)
        ).text

        logger.info(f" Success message: {success_message}")
        assert "Successfully Saved" in success_message, f"Expected success message not found: {success_message}"

        logger.info(" Test 'Add Recruitment Entry' completed successfully.")