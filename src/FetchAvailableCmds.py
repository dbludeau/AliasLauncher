import json
import re
from os import getenv


class FetchAvailableCmds:

    def __init__(self, mode):

        if mode:
            self.mode = mode
        self.data = {}

        self.list()

    def get_cmd(self):
        for line in self.data:
            yield line.strip(), self.data[line]

    def list(self):

        self.get_aliases()
        self.get_json_list()

        return self.data

    def get_aliases(self):

        # get the alaises that already exist on system
        alias_file = "%s/.bashrc" % getenv("HOME")
        with open(alias_file, "r") as text_file:
            for line in text_file:
                m = re.match('^alias(.*)=(.*)', line)
                if m:
                    self.data[m.group(1)] = m.group(2)

    def get_json_list(self):

        # get the json commands available
        with open("files/command_list.json") as data_file:
            data = json.load(data_file)

            for cmd in data[self.mode]:
                self.data[cmd] = data[self.mode][cmd]


