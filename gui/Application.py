# -*- coding: UTF-8 -*-

import kivy
from kivy.app import App
from kivy.lang import Builder
from AppLayout import AppLayout

Builder.load_file("kv/application.kv")

class Application(App):
    def build(self):
        return AppLayout()