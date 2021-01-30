from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pytest
import csv

from TestData.Data import contents
from TestData.Data import prices
from Utilities.Baseclass import BaseClass
from PageObjectModel.HomePage import Homepage
from TestData import Data
class Testcase(BaseClass):
    def test_phone(self,getData):
        for values in getData['mobilename']:
            homepage = Homepage(self.driver)
            homepage.searchSection().clear()
            homepage.searchSection().send_keys(values)
            homepage.clickAction().click()
            homepage = Homepage(self.driver)
            content = self.driver.find_elements_by_xpath(contents)
            # stars = self.driver.find_elements_by_xpath("//span[@class='a-declarative']/a/i/span")
            prices1 = self.driver.find_elements_by_xpath(prices)
            mobilename = []
            cost = []
            for i in content:
                mobilename.append(i.text)
            print('***************************')
            for price in prices1:
                cost.append(price.text)

            print(mobilename)
            print(cost)

            with open('C://Users//AL3500//Desktop//productprice.csv', 'a', encoding="utf-8", newline='') as f:
                w = csv.writer(f)
                w.writerow(["productname", "price"])
                for mobile in range(len(mobilename)):
                    for costs in range(len(cost)):
                        if (mobile == costs):
                            w.writerow([mobilename[mobile], cost[costs]])
                            break

            self.driver.refresh()

        print('i think its working fine')

    @pytest.fixture(params=[{'mobilename':['samsung','nokia','motorola']}])
    def getData(self,request):
        return request.param