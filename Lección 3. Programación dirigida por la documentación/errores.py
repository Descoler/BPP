import sys
"""
Funciones que se utilizaran para el control de errores.
-----------


Metodos
-------

NumeroErroneoColumnas:
    Recibe un número. Este error se lanzara en caso que el número de columnas de finanzas2020.csv no sea 12. 
    Se lana el mensage con el numero de mese que se han encontrado.

NoHayDatos:
    Recibe un string. Este error se lanzara en caso que alguno de los mese no tenga valores. Se lanza un mensage con el mes que no tiene datos.
"""


def NumeroErroneoColumnas(num):
    """
    Metodo lanza un mensage y cierra la aplicación cuando es lanzada al producirse el error que no hay doce meses en el archivo.
    
    Inputs
    ------
        num: Numero de columnas encontradas.
    Outputs
    -------
        Mensage de error y cierra el programa
    """
    #pass
    sys.exit(f'El numero de columnas introducidas es erroneo.\n Se eseraban 12 y se han encontrado {num}.\n Terminamos la ejecución del programa.')
        

def NoHayDatos (mes):
    """
    Metodo lanza un mensage y cierra la aplicación cuando es lanzada al producirse el error que no hay datos en uno de los meses.
    
    Inputs
    ------
        mes: Mes que no tiene datos.
    Outputs
    -------
        Mensage de error y cierra el programa.
    """
    #pass
    sys.exit(f'No hay datos en el mes de {mes}.')

# class Errores(Exception):
#     def __init__(self):
#         if self == 'NEC':
#             NEC = self.NumeroErroneoColumnas()
#         if self == 'NHD':
#             NHD = self.NoHayDatos()

    
        
    