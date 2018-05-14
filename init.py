import string
import re
import sys
import operator

l = []
k = 0
conta = 0
res = 0
op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}

def shell(prompt):
    while (True):
        str = (input(prompt))
        if str is not None:
            print(str)
            return str
        else:
            print('ERRO!')
            return None

def tokenize(expr):
    expr = expr.replace('(', ' ( ')
    expr = expr.replace(')', ' ) ')
    tokens = expr.split()
    return tokens

def isNum(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        try:
            float(s)
            return float(s)
        except ValueError:
            return s

def parseaux(i, tokens):
    global k
    global conta
    tup = ()
    while tokens[i] != ')':
        if tokens[i] == '(':
            #criar um tuplo dentro do tuplo caso encontre um novo '('
            conta = 0
            tup += (parseaux(i+1, tokens), )
            k += conta #variavel global que conta o numero de elementos apos '(' de modo a atualizar o j na funcao parse
            i += k + 1 #atualizar valor i para o elemento a seguir ao '(' que fecha este tuplo
        else:
            tup += (isNum(tokens[i]), )
            conta += 1
        i += 1
    return tup

def parse(tokens, j):
    g = []
    while (j < len(tokens)):
        if tokens[j] == '(':
            t = parseaux(j+1,tokens)
            if t != '()':
                g += [t]
        j += k + 1
    print(g)
    return g

def avalia(tuples):
    global l
    global res
    global op
    i = 0
    temp = 0
    while (i < len(tuples)):
        if (isinstance(tuples[i], tuple)):
            avalia(tuples[i])
        elif (tuples[i] == 'define'):
            l += [(tuples[i+1], tuples[i+2])]
            res = tuples[i+2]
            print(l)
        elif (isinstance(tuples[i], int) and tuples[i-2] != 'define'):
            temp = tuples[i]
            print(temp)
        elif (isinstance(tuples[i], float) and tuples[i-2] != 'define'):
            temp = tuples[i]
        elif (tuples[i] in op):
            getop = tuples[i]
            print (tuples[i])
        elif (tuples[i] == l[0][0] and tuples[i-1] != 'define'):
            res = op[getop](res,temp)
            print("res = ", res)
        i += 1
    return temp
#parse retorna lista apos parentesis, se o parse aux descobre parentisis chama parse, e necessario um contador
#str = shell('expression: ')
expr = "(define x 5) ( + (* 2 x) 7)"
print (expr)
print (tokenize(expr))
tokens = tokenize(expr)
#print (parse(tokens,0))
print(avalia(parse(tokens,0)))
k = 0
expr2 = '(define f(lambda x (+ x 2)))'
print (expr2)
print (tokenize(expr2))
tokens2 = tokenize(expr2)
print (parse(tokens2,0))
#isinstance(x,int)
#isinstance(x,float)
#isinstance(x,symbol)
#parse aux chamar recursivamente listas para formar tuplos ex: ['(','123',')','(','234',')'] = ((123),['(','234',')'])
#try return int (x); if not create exception
#(define f(lambda x (+ x 2))) = ['(','define','f','(','lambda','x','(','+','x','2',')',')',')']
# [('define', 'f')]
