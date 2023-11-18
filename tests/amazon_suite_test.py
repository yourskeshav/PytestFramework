import allure
import pytest
import time


from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.Utilities import UtilitiesPage


class Test_AmazonHomePage(BaseClass,UtilitiesPage):

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.AmazonHomeTest
    def test_verifyAmazonHomeSignInPage(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.verifySignInButtonDisplayed()
        log.info("Sign in button verified")

    ## Failed test case
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.Smoke
    @pytest.mark.AmazonHomeTest
    def test_verifyReturnAndordersButtonDisplayed(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.verifyReturnsAndOrderButtonDisplayed()
        log.info("Returns and Orders button verified")

class Test_LoginPage(BaseClass,UtilitiesPage):

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.Smoke
    @pytest.mark.AmazonHomeTest
    @pytest.mark.parametrize("username,password", [("test@gmail.com", "test123"), ("test123@gmail.com", "HelloBye")])
    def test_verifyValidationMessageIsDisplayedOnProvidingIncorrectLoginDetails(self, username, password):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        loginPage= homePage.clickSignInPageButton()
        loginPage.provideValueInEmailLoginTextField(username)
        loginPage.clickContinueButton()
        loginPage.provideValueInPasswordTextField(password)





