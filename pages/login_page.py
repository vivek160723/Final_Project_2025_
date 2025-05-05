from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username_field = (By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
        self.password_field = (By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
        self.loginBtn = (By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.error_message = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span")

    def enter_username(self,username):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self,password):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login_btn(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.loginBtn)
        ).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.error_message)
        ).text

    def login(self, username="Admin", password="admin123"):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
            )
        except:
            self.driver.save_screenshot("login_failed.png")
            raise Exception("Login failed or dashboard not loaded.")