#falta implementar '(define f(lambda x (+ x 2)))' e apresentar erro caso apareca uma variavel que nao esta na tabela

import string
import re
import sys
import operator

l = []
k = 0
conta = 0
res = 0
flag = 0
op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def shell(prompt):
    while (True):
        str = (input(prompt))
        if str is not None:
            return str
        else:
            print('ERROR: String vazia!')
            exit()

def interpreta(expr):
    global flag
    tokens = tokenize(expr)
    check(tokens)
    print("Tokenize: " + str(list(tokens)))
    tuples = parse(tokens,0)
    print("Parse: " + str(list(tuples)))
    avalia(tuples)
    if (flag == 0):
        print("Resultado = " + str(int(res)))
    else:
        print("Resultado = " + str(float(res)))

def check(tokens):
    c1 = 0
    c2 = 0
    for i in range(0,len(tokens)):
        if tokens[i] == '(':
            c1 += 1
            if tokens[i+1] != 'define' and tokens[i+1] not in op:
                print("ERROR: Nao foi possivel fazer parse dos tokens porque o elemento a seguir a '(' na string '"+str(tokens[i])+str(tokens[i+1])+"' nao e 'define' ou um operador artimetrico")
                exit()
        elif tokens[i] == ')':
            c2 += 1
    if (c1 > c2):
        print("ERROR: Existe mais '(' do que ')'");
        exit()
    elif (c2 > c1):
        print("ERROR: Existe mais ')' do que '('");
        exit()

def tokenize(expr):
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
    while j < len(tokens):
        if tokens[j] == '(':
            t = parseaux(j+1,tokens)
            if t != '()':
                g += [t]
        j += k + 1
    return g

def avalia(tuples):
    global l
    global res
    global op
    global flag
    i = 0
    temp = 0
    a = 0
    b = 0
    while (i < len(tuples)):
        if isinstance(tuples[i], tuple):
            avalia(tuples[i])
        elif tuples[i] == 'define':
            l += [(tuples[i+1], tuples[i+2])]
            #res = tuples[i+2]
        elif isinstance(tuples[i], int) and tuples[i-2] != 'define':
            temp = tuples[i]
            res = op[getop](res,temp)
        elif isinstance(tuples[i], float) and tuples[i-2] != 'define':
            temp = tuples[i]
            flag = 1
            res = op[getop](res,temp)
        elif tuples[i] in op:
            getop = tuples[i]
        elif tuples[i] == l[0][0] and tuples[i-1] != 'define':
            res = op[getop](l[0][1],temp)
        elif [a for a, b in l if tuples[i] == a] and tuples[i-1] != 'define':
            a = 0
            while (a < len(l)):
                if tuples[i] == l[a][0]:
                    b = l[a][1]
                a += 1
            temp = b
            res = op[getop](res,temp)
        i += 1

expr = shell('expressao: ')
interpreta(expr)
