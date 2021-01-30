from selenium.webdriver.common.by import By


class Homepage:

    search = (By.ID,"twotabsearchtextbox")
    click = (By.ID,"nav-search-submit-button")

    def __init__(self,driver):
        self.driver = driver

    def searchSection(self):
        return self.driver.find_element(*Homepage.search)

    def clickAction(self):
        return self.driver.find_element(*Homepage.click)


