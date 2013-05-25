import subprocess32
from baseplugins import BasePlugin
from baseplugins import add_help_text


class DediPlugin(BasePlugin):

    def __init__(self):
        add_help_text(';( dedi code\n')
        add_help_text('Example: ;(pr "hello")\n')
        self.commands = [
            (self.execDedi, {'startswith': '('}),
            (self.dedi_on, {'equals': 'dedi on'}),
            (self.dedi_off, {'equals': 'dedi off'}),
        ]

    def execDedi(self, channel, code):
        f = open('file', 'w')
        f.write(code)
        f.close()
        try:
            output = subprocess32.check_output(['dedi', 'file'], timeout=1)
            print output
            if not output.startswith('/') and\
                    not output.startswith('.') and\
                    len(output) < 512:
                self.bot.msg(channel, output)
        except Exception, exc:
            print exc
            self.bot.msg(channel, 'Exception or timeout occured')
        return True

    def dedi_on(self, channel, msg):
        self.bot.msg(channel, 'Dedi mode is open')
        self.dedi_commands = False
        return True

    def dedi_off(self, channel, msg):
        self.bot.msg(channel, 'Dedi mode is closed')
        return True
