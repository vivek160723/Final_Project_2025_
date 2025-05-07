import time
import pytest

from config import CONFIG
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.edit_employee import EditEmployeePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver_setup")
@pytest.mark.regression
@pytest.mark.smoke
class TestEditEmployee:

    def test_edit_employee_last_name(self):
        self.driver.get(CONFIG["base_url"])
        login = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        edit_emp = EditEmployeePage(self.driver)

        login.login("Admin", "admin123")
        dashboard.click_pim_from_search()
        edit_emp.search_employee("Md")
        edit_emp.click_search()
        time.sleep(3)
        edit_emp.click_edit()
        time.sleep(3)

        new_last_name = "Aghi"
        edit_emp.clear_last_name()
        time.sleep(3)
        edit_emp.update_last_name(new_last_name)
        edit_emp.save_changes()
        self.driver.refresh()


        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6"))
        # )
        #
        # updated_name = edit_emp.get_profile_header()
        # assert "Monkey lufyAghi" in updated_name, f"Expected last name '{new_last_name}' not found in profile header."
        #