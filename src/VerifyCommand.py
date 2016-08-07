import src.FetchAvailableCmds as fac
import src.RunCommand as rc


class VerifyCommand:

    def __init__(self):
        self.avail_cmds = {}
        self.cmd = ''
        self.mode = ''
        self.action = ''
        self.rc = rc.RunCommand()

    def load_available(self):
        """ We want to load the commands even if we are using
            the blacklist/nolist option.  This will contain
            aliases that are not system wide
        """
        return fac.FetchAvailableCmds(self.mode)

    def fire_cmd(self, cmd, mode):
        self.cmd = cmd.strip()
        self.mode = mode
        self.avail_cmds = self.load_available()
        print("%s running in %s mode" % (self.cmd, self.mode))

        # if we are running in whitelist, make sure this matches a pgm on the list
        if self.mode == "whitelist":
            check = self.verify_wl_ok()
            if check:
                try:
                    self.rc.set_action(self.action)
                    self.rc.start()
                    #self.rc.join()
                    #print(self.rc.stdout)
                except Exception as error:
                    raise error
        # if we are running in blacklist, see if it is on the no-no list
        elif self.mode == "blacklist":
            check = self.verify_bl_ok()
            if check:
                self.rc.start()
        # else we are running saftey off, fire the command
        elif self.mode == "nolist":
            try:
                self.rc.start()
            except Exception as error:
                raise error
        else:
            # raise ExecEception('Mode not found')
            raise Exception("Mode not found")
        # eventually run the command returning input

    def verify_wl_ok(self):
        for pgm, action in self.avail_cmds.get_cmd():
            if pgm == self.cmd:
                self.action = action
                return True
        return False

    def verify_bl_ok(self):
        print("checking the blacklist")
