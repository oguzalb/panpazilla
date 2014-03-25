Panpazilla
==========
An extendible irc bot implementation, plugin based architecture  

##Writing a plugin
    class NewPlugin(BasePlugin):

        def __init__(self):
            self.commands = [
                # Two parameters, first is the function to call,
                # Second is the rules of the command.
                # If command equals print then call print_something
                (self.print_something, {'equals':'print'}),
                # If command starts with printargs call print_arguments
                (self.print_arguments, {'startswith':'printargs '}),
                ]

        def print_something(self, channel, msg):
            self.bot.msg(channel, 'something')
            # Some commands may say 'No this is not my command'
            # even after the function called, so we should return
            # a True
            return True
            
        def print_arguments(self, channel, msg):
            self.bot.msg(channel, 'Args: ' + ' '.join(msg.split()[1:]))
            return True

Add the plugin to the plugins folder, and add it to the conf.py file  

##Currently implemented plugins:  

##=repo stats plugin=  

***Command***: *;github username repo*  
Prints watchers and stars for that repo  

##=alias plugin=  
***Command***: *;alias showpanpazilla github huseyinalb panpazilla*  
Adds showpanpazilla alias so we can shortly write ;showpanpazilla  
*;alias hello (pr "hello channel, i am panpazilla")*  
Adds hello alias so we can shortly write ;hello to exec dedi code  
***Command***: *;alias remove showpanpazilla*  
removes showpanpazilla from aliases, must be master to call this command, master is hardcoded now  
***Command***: *;aliases*  
lists aliases  

##=help plugin=
displays help, hardcoded for now  

##=dedi plugin=
A scheme subset language (Dedi Programming Language) plugin, it includes a very basic parser that ignores what it cant parse  
Dedi interpreter is included  
examples:  

* *;(pr (+ 5 (+ 2 4)))*

add 2 with 4, add with 5 and print

* *;(pr "asdasdsa")*

print this string

* *;(pr (+ "asdasda" "asdasdsa"))*

append strings and print

* *;(pr (sum (l 2 3 4)))*

find sum of the list and print

* *;(pr (h (la (l 2 3) 1)))*

add 1 to the list, take head and print it

* *;(la (l 1 2) (l 2 3))*

append lists

