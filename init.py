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
    c1 = 0
    c2 = 0
    for i in xrange(0,len(expr)):
        if expr[i] == '(':
            c1 += 1
        elif expr[i] == ')':
            c2 += 1
    if (c1 > c2):
        print("ERROR: Existe mais '(' do que ')'");
        exit()
    elif (c2 > c1):
        print("ERROR: Existe mais ')' do que '('");
        exit()
    expr = expr.replace('(', ' ( ')
    expr = expr.replace(')', ' ) ')
    tokens = expr.split()
    return tokens

def isNum(s): #verifica se e um inteiro ou um float para fazer parse
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
            if t[0] != 'define' and t[0] not in op:
                print("ERROR: Nao foi possivel fazer parse do tuplo ",t,"porque o primeiro elemento nao e 'define' nem um operador!")
                exit()
            elif t != '()':
                g += [t]
        j += k + 1
    return g

def avalia(tuples):
    global l
    global res
    global op
    i = 0
    temp = 0
    while (i < len(tuples)):
        if isinstance(tuples[i], tuple):
            avalia(tuples[i])
        elif tuples[i] == 'define':
            l += [(tuples[i+1], tuples[i+2])]
            res = tuples[i+2]
        elif isinstance(tuples[i], int) and tuples[i-2] != 'define':
            temp = tuples[i]
            res = op[getop](res,temp)
        elif isinstance(tuples[i], float) and tuples[i-2] != 'define':
            temp = tuples[i]
            res = op[getop](res,temp)
        elif tuples[i] in op:
            getop = tuples[i]
        #elif (tuples[i] == for a, b in l[a][b]) and tuples[i-1] != 'define'):
            #print("entrou")
            #res = op[getop](res,temp)
            #print("res = ", res)
        print("debug: ",tuples[i])
        i += 1
    #print("Resultado = ", res)
#parse retorna lista apos parentesis, se o parse aux descobre parentisis chama parse, e necessario um contador
#str = shell('expression: ')
#expr = "(define x 5) ( + (* 2 x) 7)"
expr = "(define x 5) (define y 2) (+ x y)"
print ("expr = " + expr)
tokens = tokenize(expr)
print("tokens = ", tokens)
tuples = parse(tokens,0)
print("parse = ", tuples)
#print (parse(tokens,0))
avalia(tuples)
print("res = ", res)
#k = 0
#expr2 = '(define f(lambda x (+ x 2)))'
#print (expr2)
#print (tokenize(expr2))
#tokens2 = tokenize(expr2)
#print (parse(tokens2,0))
#isinstance(x,int)
#isinstance(x,float)
#isinstance(x,symbol)
#parse aux chamar recursivamente listas para formar tuplos ex: ['(','123',')','(','234',')'] = ((123),['(','234',')'])
#try return int (x); if not create exception
#(define f(lambda x (+ x 2))) = ['(','define','f','(','lambda','x','(','+','x','2',')',')',')']
# [('define', 'f')]
