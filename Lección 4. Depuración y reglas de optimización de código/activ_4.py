# Ejrcicio 1
def max(list):
    x = 0
    for i in list:
        if i > x:
            x = i
    return x

def max_list(lista):
    l = []
    l = [max(item) for item in lista]
    return l

lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
# l2 = [2, 4, 1]
# print(max(lista))
maximo = max_list(lista)
print(maximo)


# Ejercicio 2
def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

l1 = [3, 4, 8, 5, 5, 22, 13]
#lres = [i for i in l1 if es_primo(i)]
lres = list(filter(es_primo,l1))
print(lres)