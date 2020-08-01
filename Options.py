# -*- coding : UTF-8 -*-

from configparser import ConfigParser

CONFIG_PATH = "config.ini"

class Options(object):
    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read(CONFIG_PATH)
        self.persons = self.parser["PersonList"]["names"].split(", ")

    def getPersons(self):
        return self.persons

    def setPersons(self, persons):
        self.persons = persons

    def save(self):
        self.parser["PersonList"]["names"] = ", ".join(self.persons)
        
        with open(CONFIG_PATH, "w") as file:
            self.parser.write(file)