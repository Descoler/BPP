def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def division(a,b):
    return (a/b) if(b!=0) else 0

def operacion_inventada(a,b,c):
    aux = division(a,b)*c
    return aux

def minimo(l):
    min = 999999999
    for i in l:
        if(i < min):
            min = i
    return min

def es_primo(n):
    primo = True

    for i in range(2, n-1):
        if (n % i == 0):
            primo = False
    
    return primo