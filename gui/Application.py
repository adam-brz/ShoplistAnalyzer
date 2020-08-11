# -*- coding: UTF-8 -*-

import kivy
from kivy.app import App
from kivy.lang import Builder
from gui.AppLayout import AppLayout
from kivy.uix.label import Label
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'kv/application.kv'))

class Application(App):
    def build(self):
        return AppLayout()