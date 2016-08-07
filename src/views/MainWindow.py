from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import src.VerifyCommand as VerifyCommand
import time


class MainWindow(GridLayout):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.cols = 1
        self.command = TextInput(hint_text='command to run', multiline=False)
        self.mode = "whitelist"
        self.command.bind(on_text_validate=self.send_cmd)
        self.add_widget(self.command)

    def send_cmd(self, cmd):
        sess = VerifyCommand.VerifyCommand()
        try:
            sess.fire_cmd(cmd.text, self.mode)
            self.command.text = ''
            self.command.hint_text = 'success'
            time.sleep(5)
            self.command.hint_text = 'command_to_run'
        except Exception as error:
            self.command.text = ''
            self.command.hint_text = 'ooops'
            time.sleep(5)
            self.command.hint_text = 'command_to_run'
