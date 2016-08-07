import subprocess
import threading


class RunCommand(threading.Thread):

    def __init__(self):
        self.action = None
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def set_action(self, action):
        self.action = action

    def run(self):

        p = subprocess.Popen(self.action,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        self.stdout, self.stderr = p.communicate()
        print("log--%s" % self.stdout)
