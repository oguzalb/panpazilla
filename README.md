panpazilla
==========

An extendible bot implementation, plugin based architecture

Plugins:

==repo stats plugin==

Command: ;github username repo

Prints watchers and start for that repo

==alias plugin==

Command: ;alias showpanpazilla github huseyinalb panpazilla

Adds showpanpazilla alias so we can shortly write ;showpanpazilla

;alias hello (pr "hello channel, i am panpazilla")

Adds hello alias so we can shortly write ;hello to exec dedi code

Command: ;alias remove showpanpazilla

removes showpanpazilla from aliases, must be master to call this command, master is hardcoded now

;aliases

lists aliases

==help plugin==
displays help, hardcoded for now

==dedi plugin==

A sceme subset language plugin, it includes a very basic parser that ignores what it cant parse

Dedi interpreter is included examples:

(pr (+ 5 (+ 2 4)))

add 2 with 4, add with 5 and print

(pr "asdasdsa")

print this string

(pr (+ "asdasda" "asdasdsa"))

append strings and print

(pr (sum (l 2 3 4)))

find sum of the list and print

(pr (h (la (l 2 3) 1)))

add 1 to the list, take head and print it

(la (l 1 2) (l 2 3))

append lists
