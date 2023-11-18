from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from allure_commons.types import AttachmentType
import allure

class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    # Locators
    signInButton = "//span[text()='Sign in']"
    returnsAndOrdersButton ="nav-orderss"
    searchSubmitButton = "nav-search-submit-button"
    searchTextField = "twotabsearchtextbox"

    # Home Page Methods

    # Method to get search icon on Amazon home page
    def getSearchSubmitButton(self):
        return self.findElementById(self.searchSubmitButton)

    # Method to click on Search Submit Button
    def clickSearchSubmitButton(self):
        self.getSearchSubmitButton().click()

    # Method to get Sign In button on Amazon home page
    def getSignInButton(self):
        return self.findElementByXpath(self.signInButton)

    # Method to verify if sign in submit is displayed
    def verifySignInButtonDisplayed(self):
        try:
            self.getSignInButton().is_displayed()
        finally:
            if(AssertionError):
                allure.attach(self.driver.get_screenshot_as_png(), name="HomePage", attachment_type=AttachmentType.PNG)

    # Click Sign in page
    def clickSignInPageButton(self):
        try:
            self.getSignInButton().click()
            loginPage = LoginPage(self.driver)
            return loginPage
        finally:
            if (AssertionError):
                allure.attach(self.driver.get_screenshot_as_png(), name="HomePage", attachment_type=AttachmentType.PNG)

    # Method to get Returns And Orders button
    def getReturnsAndOrdersButton(self):
        return self.findElementById(self.returnsAndOrdersButton)

    # Method to verify if Returns And Orders Button is displayed
    def verifyReturnsAndOrderButtonDisplayed(self):
        try:
            self.getReturnsAndOrdersButton().is_displayed()
        finally:
            if(AssertionError):
                allure.attach(self.driver.get_screenshot_as_png(), name="HomePage", attachment_type=AttachmentType.PNG)

    # Method to get searchy TextField
    def getSearchTextField(self):
        return self.findElementById(self.searchTextField)

    # Method to verify if Returns And Orders Button is displayed
    def provideValueInSearchTextField(self, productName):
        self.getSearchTextField().send_keys(productName)




