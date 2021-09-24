from selenium.webdriver.common.by import By

class HomePage():

    click_myaccount_xpath="//a[@title='My Account']"
    click_register_xpath="//a[normalize-space()='Register']"
    click_login_xpath="//li[@class='dropdown open']//li[2]//a[1]"

    def __init__(self,driver):
        self.driver=driver

    def clickMyAccount(self):
            self.driver.find_element(By.XPATH, self.click_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.click_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.click_login_xpath).click()



