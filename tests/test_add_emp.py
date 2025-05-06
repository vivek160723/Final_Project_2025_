import time

from config import CONFIG
from pages.add_emp_page import AddEmployeePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_add_employee(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    pim = PIMPage(driver)
    add_emp = AddEmployeePage(driver)

    driver.get(CONFIG["base_url"])
    login.login("Admin", "admin123")

    dashboard.search("PIM")
    dashboard.click_pim_from_search()
    time.sleep(5)
    pim.click_add_employee()
    add_emp.enter_first_name("John")
    add_emp.enter_last_name("Doe")
    add_emp.enter_employee_id("12345")
    add_emp.click_save()
