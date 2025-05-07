from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuzzPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    buzz_tab = (By.XPATH, "//span[text()='Buzz']")
    post_input = (By.XPATH, "//textarea[@placeholder=\"What's on your mind?\"]")
    post_button = (By.XPATH, "//button[normalize-space()='Post']")
    latest_post = (By.XPATH, "(//div[@class='orangehrm-buzz-post-body'])[1]")

    def go_to_buzz(self):
        buzz_element = self.wait.until(EC.presence_of_element_located(self.buzz_tab))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", buzz_element)
        self.wait.until(EC.element_to_be_clickable(self.buzz_tab)).click()

    def enter_buzz_post(self, message):
        self.wait.until(EC.visibility_of_element_located(self.post_input)).send_keys(message)

    def click_post_button(self):
        self.wait.until(EC.element_to_be_clickable(self.post_button)).click()

    def is_post_successful(self, message):
        latest_post_element = self.wait.until(EC.visibility_of_element_located(self.latest_post))
        return message in latest_post_element.text