from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
        self.last_name_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")
        self.employee_id_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
        self.save_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")

    def enter_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)

    def enter_employee_id(self, emp_id):
        emp_id_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.employee_id_input)
        )
        emp_id_input.clear()
        emp_id_input.send_keys(emp_id)

    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()