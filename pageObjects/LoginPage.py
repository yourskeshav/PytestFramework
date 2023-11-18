from utilities.BaseClass import BaseClass
import pytest

class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    # Locators
    emailTextField = "ap_email"
    continueButton ="continue"
    passwordTextField = "ap_password"

    # Home Page Methods

    # Method to get login field
    def getEmailLoginTextFeild(self):
        return self.findElementById(self.emailTextField)

    # provide values in Email text field
    def provideValueInEmailLoginTextField(self, email):
        self.getEmailLoginTextFeild().send_keys(email)

    # Method to get continue Button button on Amazon login page
    def getContinueButton(self):
        return self.findElementById(self.continueButton)

    # Method to click on Continue button
    def clickContinueButton(self):
        self.getContinueButton().click()

    # Method to get password field
    def getpasswordTextFeild(self):
        return self.findElementById(self.passwordTextField)

    # provide values in password text field
    def provideValueInPasswordTextField(self, password):
        self.getpasswordTextFeild().send_keys(password)



