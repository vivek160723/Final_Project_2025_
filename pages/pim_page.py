from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PIMPage:
    def __init__(self, driver):
        self.result_table = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span")
        self.driver = driver

    PIM_TAB = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    EMPLOYEE_LIST_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
    PAGE_HEADER = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")

    def click_pim_tab(self):
        self.driver.find_element(*self.PIM_TAB).click()

    def click_add_employee(self):
        self.driver.find_element(*self.ADD_EMPLOYEE_BUTTON).click()

    def click_employee_list(self):
        self.driver.find_element(*self.EMPLOYEE_LIST_BUTTON).click()

    def is_pim_page_displayed(self):
        return self.driver.find_element(*self.PAGE_HEADER).is_displayed()

    def click_pim_from_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.result_table)
        )
        elements = self.driver.find_elements(*self.result_table)
        for el in elements:
            if el.text.strip() == "PIM":
                el.click()
                break
