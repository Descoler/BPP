import numpy as np

def checkList(lst):
    elem = lst[0]
    resultado = True
    for i in range(1,len(lst)):
        if(lst[i] != elem):
            resultado = False
    return resultado


def tragaperras():
    operaciones = ["cereza","manzana","naranja","kiwi","melon"]
    tirada = np.random.randint(0, len(operaciones),size=len(operaciones))
    print("EL resultado de su tirada es: ")
    [print(operaciones[i]) for i in tirada]
    resultado = checkList(tirada)
    print("Ha ganado el premio") if(resultado) else print("Mala suerte, intenta de nuevo.") 

tragaperras()