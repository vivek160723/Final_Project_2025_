import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import allure

@pytest.fixture()
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = f"{rep.nodeid.replace('::', '_').replace('/', '_')}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Save screenshot
            driver.save_screenshot(file_path)


            if item.config.pluginmanager.hasplugin("html"):
                extra = getattr(rep, 'extra', [])
                from pytest_html import extras
                extra.append(extras.image(file_path))
                rep.extra = extra

            try:
                with open(file_path, "rb") as f:
                    allure.attach(
                        f.read(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                print(f"Allure screenshot attach failed: {e}")
