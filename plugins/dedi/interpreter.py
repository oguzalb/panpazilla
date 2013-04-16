import operator
from parser import make_tree

class Interpreter():
    def __init__(self):
        self.funcs = {
            '+': operator.add,
            '*': operator.mul,
            'pr': self.pr,
            'sum':self.list_sum,
            'l':self.l,
            'h':operator.itemgetter(0),
            'la':self.la,
            }
    def interpret(self, tree):
        if tree[1] == 'FUNC':
            return self.interpret(tree[0])
        params = []
        for token in tree:
        #    import pprint
        #    pprint.pprint(token)
            if token[1] == 'FUNC':
                params.append(self.interpret(token[0]))
            elif token[1]=='NUM':
                params.append(token[0])
            elif token[1]=='STR':
                params.append(token[0][1:-1])
            #print 'func: ' + str(tree[0])
            #print 'params: ' + str(params)
        return self.funcs.get(tree[0][0])(*params)
    def add(self, a, b):
        return a + b
    def mul(self, a, b):
        return a * b
    def pr(self, a):
        print(a)
    def list_sum(self, l):
        return reduce(operator.add, l)
    def l(self, *args):
        return args
    def la(self, l, *args):
        return l + args

def interpret(text):
    tree = make_tree(text)
    #from pprint import pprint
    #pprint(tree)
    interpreter = Interpreter()
    interpreter.interpret(tree[0])

def interpret_file(filename):
    #print sys.argv
    f = open(filename, 'r')
    text = f.read()
    f.close()
    interpret(text)

def test():
    interpret('(pr (+ 5 (+ 2 4)))')
    interpret('(pr "asdasdsa")')
    interpret('(pr (+ "asdasda" "asdasdsa"))')
    interpret('(pr (sum (l 2 3 4)))')
    interpret('(pr (h (la (l 2 3) 1)))')
    interpret('(la (l 1 2) (l 2 3))')

import sys
if __name__ == "__main__":
    interpret_file(sys.argv[1])
