import string
import re

#g = []
k = 0
conta = 0

'''def shell(prompt = 'expressao: '):
    while (True):
        res = parse(tokenize(input(prompt)), k)
    if res is not None:
        print(res)
    else:
        print('ERRO!')'''

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

def parseaux(i,tokens):
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
    return g

#def avalia(tuples):


#parse retorna lista apos parentesis, se o parse aux descobre parentisis chama parse, e necessario um contador
expr = "(define x 5) ( + (* 2 x) 7)"
print (expr)
print (tokenize(expr))
tokens = tokenize(expr)
print (parse(tokens,0))
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
