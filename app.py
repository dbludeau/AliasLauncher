#!/usr/bin/env python3
# app.py

import kivy
from kivy.app import App
from kivy.config import Config

import src.views.MainWindow

kivy.require('1.9.1')


class MyApp(App):

    title = 'Launcher'
    Config.set('graphics', 'width', '250')
    Config.set('graphics', 'height', '40')

    def build(self):
        return src.views.MainWindow.MainWindow()


if __name__ == '__main__':
    MyApp().run()
