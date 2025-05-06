import time
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.edit_employee import EditEmployeePage


@pytest.mark.usefixtures("driver_setup")
@pytest.mark.regression
@pytest.mark.smoke
class TestEditEmployee:

    def test_edit_employee_last_name(self):
        login = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        edit_emp = EditEmployeePage(self.driver)

        login.login("Admin", "admin123")
        dashboard.click_pim_from_search()
        edit_emp.search_employee("Amelia")
        edit_emp.click_edit()

        new_last_name = "TestLast"
        edit_emp.update_last_name(new_last_name)
        edit_emp.save_changes()
        self.driver.refresh()
        time.sleep(3)

        updated_name = edit_emp.get_profile_header()
        assert new_last_name in updated_name, f"Expected last name '{new_last_name}' not found in profile header."