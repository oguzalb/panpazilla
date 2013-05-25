import subprocess32
from baseplugins import BasePlugin


# TODO does not have a sandbox, don't use it
class PythonPlugin(BasePlugin):

    def __init__(self):
        self.commands = [
            (self.execPython, {'startswith': '>'}),
            (self.python_on, {'equals': 'python on'}),
            (self.python_off, {'equals': 'python off'}),
        ]

    def execPython(self, channel, code):
        #if self.python_commands == False:
        #    self.bot.msg(channel, 'Python modu kapali')
        if code.__contains__('exec'):
            self.bot.msg(channel, 'exec?')
        elif code.__contains__('eval'):
            self.bot.msg(channel, 'eval?')
        elif len(code) >= 64:
            self.bot.msg(channel, 'sadece 64 byte alalim beyler')
        elif code.__contains__('import'):
            self.bot.msg(channel, 'import not allowed gulum')
        else:
            f = open('file', 'w')
            f.write(code[1:])
            f.close()
            try:
                output = subprocess32.check_output(['python', 'file'],
                                                   timeout=1)
                if not output.startswith('/') and \
                        not output.startswith('.') and len(output) < 512:
                    self.bot.msg(channel, output)
            except Exception, exc:
                print exc
                self.bot.msg(channel, 'Exception or timeout occured')
        return True

    def python_on(self, channel, msg):
        self.bot.msg(channel, 'Python modu acik')
        self.python_commands = False
        return True

    def python_off(self, channel, msg):
        self.bot.msg(channel, 'Python modu kapali')
        return True
