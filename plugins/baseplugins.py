import json


class BasePlugin():
    def configure(self, bot):
        self.bot = bot


class HelpPlugin(BasePlugin):
    help_text = []

    def __init__(self):
        self.commands = [
            (self.printHelp, {'equals': 'help'}),
        ]

    @classmethod
    def add_to_help_text(cls, text):
        cls.help_text += text

    def printHelp(self, channel, msg):
        self.bot.msg(channel, ''.join(
            self.help_text + [';help shows this text\n']))
        return True


add_help_text = HelpPlugin.add_to_help_text


class AliasPlugin(BasePlugin):

    def __init__(self):
        add_help_text(';aliases lists the aliases\n')
        add_help_text(';alias alias_name command adds the alias\n')
        add_help_text('Example: ;alias hello (pr "hello")\n')
        add_help_text(
            'Example: ;alias panpazilla github huseyinalb panpazilla\n')
        add_help_text(';alias_remove alias_name removes the alias\n')

        self.aliasCommands = {'kulekacoldu': 'github fatiherikli kule',
                              'simmetricakacoldu': 'github import simmetrica'}
        self.commands = [
            (self.printAliases, {'equals': 'aliases'}),
            (self.add_to_aliases, {'startswith': 'alias '}),
            (self.alias_command, {}),
            (self.alias_remove, {'startswith': 'alias_remove', 'admin': True})
        ]
        f = open('alias_commands', 'r')
        fcontent = f.read()
        f.close()
        try:
            aliasCommands = json.loads(fcontent)
            for alias, command in aliasCommands.items():
                self.aliasCommands[
                    alias.encode('utf-8')] = command.encode('utf-8')
        except ValueError, e:
            print e
            pass

    def printAliases(self, channel, msg):
        for alias, command in self.aliasCommands.items():
            self.bot.msg(
                channel, r'alias: %s command: %s' % (alias, command))
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
            self.bot.msg(
                channel,
                ';alias kisayol komut parametreler seklinde olmali yegen')
            return False

    def alias_command(self, channel, msg):
        command = msg.split()[0]
        if self.aliasCommands.get(command, False):
            self.bot.processPluginCommands(
                channel, self.aliasCommands[command])
            return True
        return False

    def alias_remove(self, channel, msg):
        alias_name = msg.split()[1]
        if alias_name in self.aliasCommands:
            del self.aliasCommands[alias_name]
            self.bot.msg(channel,
                         '%s elayisi silindi' % (alias_name,))
        else:
            self.bot.msg(
                channel,
                '%s diye bir elayis yok element uydurma' % (alias_name,))
        return True
