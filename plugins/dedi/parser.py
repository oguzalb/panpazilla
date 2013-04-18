import re

patterns = [('\(', 'OPAR'),
            ('\)', 'CPAR'),
            ('[\-_A-Za-z\+\-][\-_A-Za-z0-9]*', 'IDEN'),
            ('[0-9]+', 'NUM'),
            ('"[^"]*"', 'STR'),
            ]

def lex(text):
    return[i for i in re.findall('('+ '|'.join([i[0] for i in patterns]) +')',text)]

def identify(lexam):
    for pattern in patterns:
        if re.match(pattern[0], lexam):
            if pattern[1] == 'NUM':
                lexam = int(lexam)
            return lexam, pattern[1]

def tokenize(lexams):
    for i in lexams:
        yield identify(i)

class TreeMaker():
    def __init__(self, tokens):
        self.tokens = tokens
    def create_node(self):
        children = []
        for i in self.tokens:
            if i[1] == 'OPAR':
                children += [[self.create_node(), 'FUNC']]
            elif i[1] == 'CPAR':
                break
            else:
                children += [i]
        return children


def make_tree(text):
    return TreeMaker(tokenize(lex(text))).create_node()
