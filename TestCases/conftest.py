import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture()
def setUp(request):
    browser_name=request.config.getoption("browser_name")
    if(browser_name=='chrome'):
        driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe')


    elif(browser_name =='ie'):
        driver = webdriver.Ie(executable_path='D:/IEDriverServer_x64_3.150.1/IEDriverServer.exe')
    elif(browser_name =='firefox'):
        driver = webdriver.Firefox(executable_path="D:/geckodriver-v0.29.0-win64/geckodriver.exe")


    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()




