import json


class BasePlugin():
    def configure(self, bot):
        self.bot = bot


class HelpPlugin(BasePlugin):

    def __init__(self):
        self.commands = [
            (self.printHelp, {'equals':'help'}),
            ]

    def printHelp(self, channel, msg):
        self.bot.msg(channel, ';> ile baslayan 64 bytelik python kodlarinin ciktisini doner\n' + \
                              ';github username repo\n' + \
                              ';alias command param1 param2 ... komut icin kisayol olusturur\n' + \
                              ';aliases daha once olusturulmus komutlari listeler\m' + \
                              ';help bu yaziyi gosterir')
        return True


class AliasPlugin(BasePlugin):

    def __init__(self):
        self.aliasCommands = {'kulekacoldu':'github fatiherikli kule',
                              'simmetricakacoldu':'github import simmetrica'}
        self.commands = [
            (self.printAliases, {'equals':'aliases'}),
            (self.add_to_aliases, {'startswith':'alias '}),
            (self.alias_command, {}),
            (self.alias_remove, {'startswith':'alias_remove', 'admin':True})
        ]
        f = open('alias_commands','r')
        fcontent = f.read()
        f.close()
        try:
            print fcontent
            aliasCommands = json.loads(fcontent)
            print aliasCommands
            for alias, command in aliasCommands.items():
                self.aliasCommands[alias.encode('utf-8')] = command.encode('utf-8')
        except ValueError, e:
            print e
            pass

    def printAliases(self, channel, msg):
        for alias, command in self.aliasCommands.items():
            self.bot.msg(channel, r'alias: %s command: %s' % (alias, command))
        return True

    def add_to_aliases(self, channel, msg):
        tokens = msg.split()
        if len(tokens) > 2:
            shortcut = tokens[1]
            command = ' '.join(tokens[2:])
            self.aliasCommands[shortcut] = command
            f = open('../alias_commands', 'w')
            f.write(json.dumps(self.aliasCommands))
            f.close()
            self.bot.msg(channel, command + ' elayislara eklendi')
            return True
        else:
            self.bot.msg(channel, ';alias kisayol komut parametreler seklinde olmali yegen')
            return False

    def alias_command(self, channel, msg):
        command = msg.split()[0]
        print command
        print self.aliasCommands
        if self.aliasCommands.get(command, False):
            print 'comm:' + self.aliasCommands[command]
            self.bot.processPluginCommands(channel, self.aliasCommands[command])
            return True
        return False

    def alias_remove(self, channel, msg):
        alias_name = msg.split()[1]
        if self.aliasCommands.has_key(alias_name):
            del self.aliasCommands[alias_name]
            self.bot.msg(channel, '%s elayisi silindi' % (alias_name,))
        else:
            self.bot.msg(channel, '%s diye bir elayis yok element uydurma' % (alias_name,))
        return True
