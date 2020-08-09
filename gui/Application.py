# -*- coding: UTF-8 -*-

import kivy
from kivy.app import App
from AppLayout import AppLayout
from kivy.lang import Builder

Builder.load_file("kv/application.kv")

class Application(App):
    def build(self):
        return AppLayout()