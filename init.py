import string
import re

g = []
j = 0

def tokenize(expr):
    expr = expr.replace('(', '( ')
    expr = expr.replace(')', ' )')
    tokens = expr.split()
    return tokens

def parseaux(i,tokens):
    #if tokens[i] == '(' -> while loop
    return l

def parse(tokens, j):
    while (i < len(tokens)):
        (j,t) = parseaux(i,tokens)
        g = [t] + g


expr = "(define x 5) ( + (* 2 x) 7)"
print (expr)
print (tokenize(expr))
tokens = tokenize(expr)
print (parseaux(tokens))

#isinstance(x,int)
#isinstance(x,float)
#isinstance(x,symbol)
#parse aux chamar recursivamente listas para formar tuplos ex: ['(','123',')','(','234',')'] = ((123),['(','234',')'])
#try return int (x); if not create exception
