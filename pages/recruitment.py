import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger

logger = setup_logger("Recruit")

class Recruit:
    def __init__(self, driver):
        self.driver = driver
        self.recruitementbutton = (By.XPATH, "//span[text()='Recruitment']")
        self.addbutton = (By.XPATH, "//button[normalize-space()='Add']")
        self.firstname = (By.NAME, "firstName")
        self.lastname = (By.NAME, "lastName")
        self.email = (By.XPATH, "//label[text()='Email']/../following-sibling::div/input")
        self.jobvacancydd = (By.XPATH, "//label[text()='Vacancy']/../following-sibling::div//div[contains(@class, 'oxd-select-text')]")
        self.vacancy = (By.XPATH, "//div[@role='option']/span[text()='Software Engineer']")
        self.savebutton = (By.XPATH, "//button[normalize-space()='Save']")
        self.successmessage = (By.XPATH, "//div[contains(@class,'oxd-toast-content')]")

    def click_recruitment(self):
        logger.info("Clicking on 'Recruitment' tab")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.recruitementbutton)
        ).click()

    def click_add_button(self):
        logger.info("Clicking on 'Add' button")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.addbutton)
        ).click()

    def enter_first_name(self, fname):
        logger.info(f"Entering first name: {fname}")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.firstname)
        ).send_keys(fname)

    def enter_last_name(self, lname):
        logger.info(f"Entering last name: {lname}")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.lastname)
        ).send_keys(lname)

    def enter_email(self, eid):
        logger.info(f"Entering email ID: {eid}")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email)
        ).send_keys(eid)

    def select_job_vacancy(self):
        logger.info("Selecting 'Software Engineer' from vacancy dropdown")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.jobvacancydd)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.vacancy)
        ).click()

    def click_save_button(self):
        logger.info("Clicking on 'Save' button")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.savebutton)
        ).click()

    def get_success_message(self):
        logger.info("Retrieving success message after saving")
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.successmessage)
        ).text