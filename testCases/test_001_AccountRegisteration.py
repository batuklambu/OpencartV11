import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegisterationPage
from utilities import randomeString
import os
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen() # for logging

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info('**** test_001_Account Registeration is started')
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Launching Browser")

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Providing Personal information")
        self.regpage=AccountRegisterationPage(self.driver)
        self.regpage.setFirstName("Scott")
        self.regpage.setLastName("Morris")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("2039899010")
        self.regpage.setPassword("admin")
        self.regpage.setConfirmPwd("admin")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        self.logger.info("Account registeration is passed")
        if self.confmsg=="Your Account Has Been Created!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.error("Account registeration failed")
            self.driver.close
            assert False
        self.logger.info("Account registeration finished")