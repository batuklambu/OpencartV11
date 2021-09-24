from selenium.webdriver.common.by import By

class AccountRegisterationPage():

    txtbox_firstname_id = "input-firstname"
    txtbox_lastname_id = "input-lastname"
    txtbox_email_id = "input-email"
    txtbox_telephone_id = "input-telephone"
    txtbox_password_id = "input-password"
    txtbox_pwdconfirm_id = "input-confirm"
    txt_confpassword_name = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath="//input[@value='Continue']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"


    def __init__(self,driver):
        self.driver=driver

    def setFirstName(self,firstname):
        firstnametxt=self.driver.find_element(By.ID,self.txtbox_firstname_id)
        firstnametxt.send_keys(firstname)

    def setLastName(self,lastname):
        lastnametxt=self.driver.find_element(By.ID,self.txtbox_lastname_id)
        lastnametxt.send_keys(lastname)

    def setEmail(self,email):
        emailtxt=self.driver.find_element(By.ID,self.txtbox_email_id)
        emailtxt.send_keys(email)

    def setTelephone(self,telephone):
        telephonetxt=self.driver.find_element(By.ID,self.txtbox_telephone_id)
        telephonetxt.send_keys(telephone)

    def setPassword(self,password):
        passwordtxt=self.driver.find_element(By.ID,self.txtbox_password_id)
        passwordtxt.send_keys(password)

    def setConfirmPwd(self,pwdconfirm):
        pwdconfirmtxt=self.driver.find_element(By.ID,self.txtbox_pwdconfirm_id)
        pwdconfirmtxt.send_keys(pwdconfirm)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME,self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_cont_xpath).click()

    def getconfirmationmsg(self):
        try:
            return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None

