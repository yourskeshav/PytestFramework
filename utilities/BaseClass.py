import inspect
import logging
import pytest
from selenium.webdriver.support.select import Select
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from tests.conftest import log

@pytest.mark.usefixtures("setup")
class BaseClass():

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def presenceOfElementLocated(self, Locator, elementID):
         try:
            if Locator == 'Id':
                locatorById = By.ID
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorById, elementID)))

            elif Locator == 'Name':
                locatorByName = By.NAME
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorByName, elementID)))

            elif Locator == 'ClassName':
                locatorByClass = By.CLASS_NAME
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorByClass, elementID)))

            elif Locator == 'Css':
                locatorByCss = By.CSS_SELECTOR
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorByCss, elementID)))

            elif Locator == 'xpath':
                locatorByXpath = By.XPATH
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorByXpath, elementID)))

            elif Locator == 'linkText':
                locatorLinkText = By.LINK_TEXT
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorLinkText, elementID)))
         except TimeoutException:
             log.info('Timed out waiting for page to load')

    def waitForPageToLoad(self, Locator, elementID):
        self.presenceOfElementLocated(Locator, elementID)

    def waitForElement(self, Locator, elementID):
        self.presenceOfElementLocated(Locator, elementID)

    def waitForElementToBeVisible(self, Locator, elementID):
        driver = WebDriverWait(self.driver, 10)
        try:
            if Locator == 'Id':
                locatorById = By.ID
                driver.until(EC.visibility_of_element_located((locatorById, elementID)))

            elif Locator == 'Name':
                locatorByName = By.NAME
                driver.until(EC.visibility_of_element_located((locatorByName, elementID)))

            elif Locator == 'ClassName':
                locatorByClass = By.CLASS_NAME
                driver.until(EC.visibility_of_element_located((locatorByClass, elementID)))

            elif Locator == 'Css':
                locatorByCss = By.CSS_SELECTOR
                driver.until(EC.visibility_of_element_located((locatorByCss, elementID)))

            elif Locator == 'xpath':
                locatorByXpath = By.XPATH
                driver.until(EC.visibility_of_element_located((locatorByXpath, elementID)))

            elif Locator == 'linkText':
                locatorLinkText = By.LINK_TEXT
                driver.until(EC.visibility_of_element_located((locatorLinkText, elementID)))

        except TimeoutException:
            log.info('Timed out while waiting for visibility of web-element')

    def waitForElementToBeClickable(self, Locator, elementID):
        driver = WebDriverWait(self.driver, 10)
        try:
            if Locator == 'Id':
                locatorById = By.ID
                driver.until(EC.element_to_be_clickable((locatorById, elementID)))

            elif Locator == 'Name':
                locatorByName = By.NAME
                driver.until(EC.element_to_be_clickable((locatorByName, elementID)))

            elif Locator == 'ClassName':
                locatorByClass = By.CLASS_NAME
                driver.until(EC.element_to_be_clickable((locatorByClass, elementID)))

            elif Locator == 'Css':
                locatorByCss = By.CSS_SELECTOR
                driver.until(EC.element_to_be_clickable((locatorByCss, elementID)))

            elif Locator == 'xpath':
                locatorByXpath = By.XPATH
                driver.until(EC.element_to_be_clickable((locatorByXpath, elementID)))

            elif Locator == 'linkText':
                locatorLinkText = By.LINK_TEXT
                driver.until(EC.element_to_be_clickable((locatorLinkText, elementID)))

        except TimeoutException:
            log.info('Timed out while waiting for web-element to be clickable')

    def waitForElementToBeInvisible(self, Locator, elementID):
        driver = WebDriverWait(self.driver, 10)
        try:
            if Locator == 'Id':
                locatorById = By.ID
                driver.until(EC.invisibility_of_element_located((locatorById, elementID)))

            elif Locator == 'Name':
                locatorByName = By.NAME
                driver.until(EC.invisibility_of_element_located((locatorByName, elementID)))

            elif Locator == 'ClassName':
                locatorByClass = By.CLASS_NAME
                driver.until(EC.invisibility_of_element_located((locatorByClass, elementID)))

            elif Locator == 'Css':
                locatorByCss = By.CSS_SELECTOR
                driver.until(EC.invisibility_of_element_located((locatorByCss, elementID)))

            elif Locator == 'xpath':
                locatorByXpath = By.XPATH
                driver.until(EC.invisibility_of_element_located((locatorByXpath, elementID)))

            elif Locator == 'linkText':
                locatorLinkText = By.LINK_TEXT
                driver.until(EC.invisibility_of_element_located((locatorLinkText, elementID)))

        except TimeoutException:
            log.info('Timed out while waiting for invisibility of web-element')

    def getTitle(self):
        self.driver(self).title()

    """All the find element selenium properties"""

    def findElementById(self, Id):
        Locator = By.ID
        self.isElementPresent(Locator, Id)
        return self.driver.find_element_by_id(Id)

    def findElementByName(self, Name):
        Locator = By.NAME
        self.isElementPresent(Locator, Name)
        log.info(self.driver)
        return self.driver.find_element_by_name(Name)

    def findElementsByName(self, Name):
        Locator = By.NAME
        self.isElementPresent(Locator, Name)
        return self.driver(self).find_elements_by_name(Name)

    def findElementByXpath(self, Xpath):
        Locator = By.XPATH
        self.isElementPresent(Locator, Xpath)
        return self.driver.find_element_by_xpath(Xpath)

    def isDisplayed(self):
        return self.is_displayed()

    def findElementsByXpath(self, Xpath):
        Locator = By.XPATH
        self.isElementPresent(Locator, Xpath)
        return self.driver.find_elements_by_xpath(Xpath)

    def findElementByCSS(self, CSS):
        Locator = By.CSS_SELECTOR
        self.isElementPresent(Locator, CSS)
        return self.driver.find_element_by_css_selector(CSS)

    def findElementsByCSS(self, CSS):
        Locator = By.CSS_SELECTOR
        self.isElementPresent(Locator, CSS)
        return self.driver.find_elements_by_css_selector(CSS)

    def findElementsByClassName(self, ClassName):
        Locator = By.CLASS_NAME
        self.isElementPresent(Locator, ClassName)
        return self.driver.find_elements_by_class_name(ClassName)

    def findElementByClassName(self, ClassName):
        Locator = By.CLASS_NAME
        self.isElementPresent(Locator, ClassName)
        return self.driver.find_element_by_class_name(ClassName)

    def findElementByLinkText(self, LinkText):
        Locator = By.LINK_TEXT
        self.isElementPresent(Locator, LinkText)
        return self.driver.find_element_by_link_text(LinkText)

    def findElementsByLinkText(self, LinkText):
        Locator = By.LINK_TEXT
        self.isElementPresent(Locator, LinkText)
        return self.driver.find_elements_by_link_text(LinkText)

    def findElementByPartialLinkText(self, PartialLinkText):
        Locator = By.PARTIAL_LINK_TEXT
        self.isElementPresent(Locator, PartialLinkText)
        return self.driver.find_element_by_partial_link_text(PartialLinkText)

    def findElementsByPartialLinkText(self, PartialLinkText):
        Locator = By.PARTIAL_LINK_TEXT
        self.isElementPresent(Locator, PartialLinkText)
        return self.driver.find_elements_by_partial_link_text(PartialLinkText)

    def findElementByTagName(self, tagName):
        Locator = By.TAG_NAME
        self.isElementPresent(Locator, tagName)
        return self.driver.find_element_by_tag_name(tagName)

    def findElementsByTagName(self, tagName):
        Locator = By.TAG_NAME
        self.isElementPresent(Locator, tagName)
        return self.driver.find_elements_by_tag_name(tagName)

    def hover(self, Locator, locator_value):
        element = self.find_element(by=Locator, value=locator_value)
        ActionChains(self.driver).move_to_element(element).perform()

    def hoverAndClick(self, Locator, locator_value):
        element = self.driver.find_element(by=Locator, value=locator_value)
        ActionChains(self.driver).move_to_element(element).perform().click()

    def doubleClick(self, Locator, locator_value):
        element = self.driver.find_element(by=Locator, value=locator_value)
        ActionChains(self.driver).move_to_element(element).perform().doubleClick()

    def scrollToView(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scrollToGetElement(self, element):
        self.driver.execute_script("arguments[0].focus();", element)

    def refreshPage(self):
        self.driver.refresh()

    def isElementPresent(self, Locator, locator_value):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=Locator, value=locator_value)
            return True
        except NoSuchElementException:
            return False

    def wait_Until(self, sec):
        time.sleep(sec)

    def WaitToChangeUrl(self, changed_url):
        driver = WebDriverWait(self.driver, 20)
        try:
            driver.until(EC.url_changes(changed_url))
        except TimeoutException:
            log.info('Timed out while waiting for invisibility of web-element')

    def waitForReady(self):
        driver = WebDriverWait(self.driver, 35)
        try:
            driver.until(lambda d: d.execute_script("return jQuery.active == 0"))
        except TimeoutException:
            log.info('Timed out while waiting for invisibility of web-element')

    def scrollToViewElement(self):
        self.driver.execute_script("window.scrollBy(0, -50);")

    def element_in_viewport(self, elem):
        elem_left_bound = elem.location.get('x')
        elem_top_bound = elem.location.get('y')
        elem_width = elem.size.get('width')
        elem_height = elem.size.get('height')
        elem_right_bound = elem_left_bound + elem_width
        elem_lower_bound = elem_top_bound + elem_height

        win_upper_bound = self.driver.execute_script('return window.pageYOffset')
        win_left_bound = self.driver.execute_script('return window.pageXOffset')
        win_width = self.driver.execute_script('return document.documentElement.clientWidth')
        win_height = self.driver.execute_script('return document.documentElement.clientHeight')
        win_right_bound = win_left_bound + win_width
        win_lower_bound = win_upper_bound + win_height

        return all((win_left_bound <= elem_left_bound,
                    win_right_bound >= elem_right_bound,
                    win_upper_bound <= elem_top_bound,
                    win_lower_bound >= elem_lower_bound)
                   )

    def getCurrentUrl(self):
        currentURl = self.driver.current_url
        return  currentURl

    def NavigateToURL(self, url):
        self.driver.get(url)

    def switchToDiffrentTab(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
