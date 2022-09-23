import pytest
from selenium import webdriver
# We need to fetch all action from another page
# import configtest
from pageObjects.LoginPage import Login
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_002_DDT_Login:

    baseurl = Readconfig.getApplicationURL()
    username = Readconfig.getLoginEmail()
    password = Readconfig.getLoginPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*********************Test_001_Login**************************")
        # Launch driver
        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        if actual_title=="Your store. Login":
            self.driver.close()
            self.logger.info("*******************Home Page Title Test Passed*******************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle1.png")
            self.driver.close()
            self.logger.info("*******************Home Page Title Test Failed*******************")
            assert False

    def test_login(self,setup):

        self.driver = setup
        self.driver.get(self.baseurl)
        # Create object of login page
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        homepagetitle =self.driver.title
        if homepagetitle=="Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("*******************Login Test Passed*******************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login1.png")
            self.driver.close()
            self.logger.info("*******************Login Test Failed*******************")
            assert False

