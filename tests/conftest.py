import os
from datetime import datetime
import sys
from urllib import request

import allure
import pytest
import logging

import pytest_html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from testData.PropertyLoader import PropertyLoader

driver = None

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(message)s'))
out_hdlr.setLevel(logging.DEBUG)
log.addHandler(out_hdlr)
log.setLevel(logging.DEBUG)

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--env_name", action="store", default="US"
    )


@pytest.fixture(params=["chrome"],scope="function")   # fixture paramterization we have to use params
def setup(request):
    global driver
    # global driver
    env_name = request.config.getoption("--env_name")

    # invoke driver using webdriver manager
    if request.param == "chrome":     # fixture paramterization
        s = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=s, options=chrome_options)

    # invoke firefox driver using webdriver manager
    if request.param == "firefox":
        s = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)

    if env_name == "US":
        driver.get(PropertyLoader.getUnitedStatesUrl())
    elif env_name == "India":
        driver.get(PropertyLoader.getIndiaURL())


    # driver.get(PropertyLoader.getURL())
    driver.maximize_window()

    # driver is sent to class object  =driver(local driver) and cls.driver(class driver)
    request.cls.driver = driver
    driver.implicitly_wait(2)

    #tear-down method to close and quit the browser
    yield
    driver.quit()


@pytest.mark.hookwrapper  # this piece of code is required to generate html report
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (
            "report_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )

