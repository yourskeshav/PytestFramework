import configparser
import os
import logging

class PropertyLoader:

    @staticmethod    
    def getPropfile(SectionName,PropertyName):
        config = configparser.RawConfigParser()
        cur = os.path.dirname(os.path.abspath(__file__))
        config.read(os.path.join(cur, 'config.cfg'))        
        prop = config.get(SectionName, PropertyName)
        return prop          
           
    @staticmethod 
    def getIndiaURL():
        return PropertyLoader.getPropfile('url_details','India_Url')
        
    @staticmethod
    def getUnitedStatesUrl():
        return PropertyLoader.getPropfile('url_details','UnitedStates_URL')
