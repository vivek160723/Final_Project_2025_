import time

from config import CONFIG
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.dashboard_page import DashboardPage

def test_pim_page_navigation_using_search(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    pim = PIMPage(driver)
    driver.get(CONFIG["base_url"])
    login.login("Admin", "admin123")
    dashboard.search("PIM")
    pim.click_pim_from_search()
    time.sleep(3)
    assert pim.is_pim_page_displayed(), "PIM Page did not load"