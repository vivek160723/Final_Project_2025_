from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/div/div/input")
        self.result_table = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span")

    def search(self, keyword):
        search_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_input)
        )
        search_element.clear()
        search_element.send_keys(keyword)

    def click_pim_from_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.result_table)
        )
        elements = self.driver.find_elements(*self.result_table)
        for el in elements:
            if el.text.strip() == "PIM":
                el.click()
                break