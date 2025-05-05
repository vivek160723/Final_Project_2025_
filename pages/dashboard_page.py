from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/div/div/input")
        self.result_table = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span")

    # def search(self, keyword):
    #     search_element = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(self.search_input)
    #     )
    #     search_element.clear()
    #     search_element.send_keys(keyword)
    #
    #     # Wait for results to appear
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(self.result_table)
    #     )

    def search(self, keyword):
        search_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_input)
        )
        search_element.clear()
        search_element.send_keys(keyword)