from datetime import datetime
import random
import time
import logging

from datetime import date
import datetime
from datetime import timedelta
import random
import time
import logging
import pytest

class UtilitiesPage ():

    CHAR_LIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    '''
    Method to generate random alphabetic string of 6 characters
    @rtype:   str
    @return:  randStr
    '''
    @staticmethod
    def generateRandomString():
        RANDOM_STRING_LENGTH = 6
        randStr = ''
        for i in range(RANDOM_STRING_LENGTH):
            number = UtilitiesPage.getRandomNumber()
            ch = UtilitiesPage.CHAR_LIST.__getitem__(number)
            randStr=randStr+ch

        return randStr

    '''
    Method to generate a random number
    @rtype:   int
    @return:  randomInt
    '''
    @staticmethod
    def getRandomNumber():
        randomGenerator = random
        randomInt = randomGenerator.randint(0, len(UtilitiesPage.CHAR_LIST))
        if randomInt - 1 == -1:
            return randomInt
        else:
            return randomInt - 1

    '''
    Method to return a filename of {folder}/{classname}.{method}-window{windowid}-{timestamp} format
    @rtype:   str
    @return:  filename
    '''

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return "{folder}/{classname}.{method}-window{windowid}-{timestamp}".format(
            folder=self.SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
    )


    #method to switch between tab on element
    def switch_to_tab(self):
        window_before = self.getDriver().GET_WINDOW_HANDLES()
        logging.info(window_before)
        window_after = self.getDriver().window_handles[1]
        logging.info(window_after)
        self.getDriver().switch_to_window(window_after)
        time.sleep(1)


    @staticmethod
    def generateRandomNumber(x):
        """Return an X digit number, leading_zeroes returns a string, otherwise int"""
        leading_zeroes=False
        if not leading_zeroes:
        # wrap with str() for uniform results
            return random.randint(10**(x-1), 10**x-1)
        else:
            if x > 6000:
                return ''.join([str(random.randint(0, 9)) for i in range(x)])
            else:
                return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)



    @staticmethod
    def generate_RandomString(X):
        RANDOM_STRING_LENGTH = X
        randStr = ''
        for i in range(RANDOM_STRING_LENGTH):
            number = UtilitiesPage.getRandomNumber()
            ch = UtilitiesPage.CHAR_LIST.__getitem__(number)
            randStr=randStr+ch

    def getCurrentDate(self):
        today = date.today()
        return(today.strftime("%Y-%m-%d"))      #2022-01-25

    def getCurrentDateWithForwardSlash(self):
        today = date.today()
        return(today.strftime("%m/%d/%Y"))      #02/02/1997

    def addDaysToDate(self, daysToAdd):
        todayDate = self.getCurrentDate()
        currentTime = datetime.datetime.strptime(todayDate, "%Y-%m-%d")
        updatedDateTime = currentTime + datetime.timedelta(days=daysToAdd)
        return(updatedDateTime.strftime("%Y-%m-%d"))

    def getCurrentDateTime(self):
        dateTime =  datetime.datetime.now()
        todayDateTime = dateTime.strftime("%a %m/%d/%Y %#I:%M %p")  #Fri 05/20/2022 2:40 PM
        return (todayDateTime)
