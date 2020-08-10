# -*- coding : UTF-8 -*-

from configparser import ConfigParser

CONFIG_PATH = "config.ini"

class Options(object):
    def __init__(self):
        self.persons = []
        self.parser = ConfigParser()
        self.parser.read(CONFIG_PATH)

        try:
            self.setPersonsFromString(self.parser["PersonList"]["names"])
        except KeyError:
            self.persons = ["Me"]

    def getPersons(self):
        return self.persons

    def getPersonsString(self):
        return ", ".join(self.persons)

    def setPersonsFromString(self, persons_string):
        self.persons = [person.strip() for person in persons_string.split(",")]

    def setPersons(self, persons):
        self.persons = persons

    def save(self):
        if not self.parser.has_section("PersonList"):
            self.parser.add_section("PersonList")

        self.parser["PersonList"]["names"] = self.getPersonsString()

        with open(CONFIG_PATH, "w") as file:
            self.parser.write(file)