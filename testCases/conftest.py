from selenium import webdriver
import pytest


@pytest.fixture

def setup(browser):
    if browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    return driver

# This will get the value from CLI (command line)/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

# After getting value from command line we need to pass the value to set up method.
# This fixture will return the browser value to set up method
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

# ************Pytest htlml report************

def pytest_configure(config):
    # Hook for adding environment info to HTML Report
    config._metadata['Project Name']= 'nopCommerce'
    config._metadata['Module Name']= 'Customers'
    config._metadata['Tester']= 'Deepa'

    # Hook for Delete/Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
