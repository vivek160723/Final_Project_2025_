from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    search_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input")
    search_result = (By.XPATH, "//div[@role='listbox']//span")
    search_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    edit_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i")
    last_name_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input")
    save_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button")
    profile_name = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6")

    def search_employee(self, name):
        self.wait.until(EC.visibility_of_element_located(self.search_input)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.search_result)).click()

    def click_edit(self):
        self.wait.until(EC.element_to_be_clickable(self.edit_button)).click()

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()


    def clear_last_name(self):
        last_name_field = self.wait.until(EC.visibility_of_element_located(self.last_name_input))
        last_name_field.clear()


    def update_last_name(self, new_last_name):
        last_name_field = self.wait.until(EC.visibility_of_element_located(self.last_name_input))
        last_name_field.clear()
        last_name_field.send_keys(new_last_name)

    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def get_profile_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.profile_name)).text