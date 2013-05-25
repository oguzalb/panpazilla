from twisted.words.protocols import irc
from twisted.internet import protocol
import conf


class Panpazilla(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)
    python_commands = True

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        # TODO may have problems in multiple channels
        plugins = conf.plugins
        self.commands = []
        for plugin in plugins:
            pluginInstance = plugin()
            pluginInstance.configure(self)
            self.commands += pluginInstance.commands
            print self.commands
        print "Joined %s." % (channel,)

    def kickedFrom(self, channel, kicker, message):
        self.join(channel)
        self.msg(channel, kicker + ' why why why??')

    def processPluginCommands(self, channel, msg, admin=False):
        processed_command = False
        for command in self.commands:
            command_rules = command[1]
            rule_ok = True
            for key, val in command_rules.items():
                print key, val
                if key == 'startswith':
                    rule_ok = msg.startswith(val) and rule_ok
                elif key == 'equals':
                    rule_ok = (msg == val) and rule_ok
                elif key == 'admin':
                    rule_ok = admin and rule_ok
            if rule_ok:
                print 'running' + str(command[0])
                processed_command = command[0](channel, msg)
                if processed_command:
                    break
        if not processed_command:
            self.msg(channel, 'Could\'t understand the command')

    def privmsg(self, user, channel, msg):
        print msg
        if msg.startswith(self.factory.nickname+':'):
            self.msg(channel, msg[len(self.factory.nickname):])
        elif msg.startswith(';'):
            self.processPluginCommands(channel, msg[1:])


class PanpazillaBotFactory(protocol.ClientFactory):
    protocol = Panpazilla

    def __init__(self, channel, nickname='HusBot'):
        self.channel = channel
        self.nickname = nickname

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)


from twisted.internet import reactor

if __name__ == "__main__":
    chan = 'suveys'
    reactor.connectTCP('irc.freenode.net', 6667, PanpazillaBotFactory(chan))
    reactor.run()
