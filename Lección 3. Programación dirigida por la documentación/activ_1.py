from os import name
from typing import Type
import pandas as pd
import numpy as nm
import sys
from pandas.core.frame import DataFrame
from pandas.core.indexes.numeric import Int64Index
from pandas.core.indexing import IndexingMixin
import errores as er

"""
Calculo sobre archivo finanzas2020.csv
Descripcion
-----------
Realizaremos diferentes cálculos sobre el archivo finazas 2020, 
asi como el control de los posibles errores que nos pudierean dar tanto los datos como las operaciones.

Metodos
-------

validaTipos:
    Recibe una lista de valores y ha de devolver una lista de valores de tipo np.int64. Controlando todos los errores que puedan surgir.

validaSiHayDatos:
    Recibe un dataframe y valida que todos los meses tengan algun dato, tambien llama a la funcion validaTipos para comprobar los tipos 
    de datos pasados por cada mes

"""
def validaTipos(lista):
    """
    Metodo valida tipos. Devuelve una lista de valores de tipo numpy.int64, en los valores que den error se devuelve un 0.
    Inputs
    ------
        lista: lista de valores a validar.
    Outputs
    -------
        list: lista de valores validados.
    """
    list = []
    for item in lista:
        try:
            list.append(nm.int64(item))
        except ValueError as e:
            list.append(0)
    return list

def validaSiHayDatos(dataFr): 
    """
    Metodo valida tipos. Devuelve una lista de valores de tipo np.int64, en los valores que den error se devuelve un 0.
    Inputs
    ------
        dataFr: pandas.Dataframe con los valores extraidos del archivo finanzas2020.csv.
    Outputs
    -------
        dataFr: pandas.DataFrame con los valores validaddos (que los meses tengan datos y que sean numpy.int64)
    """
    for mes in dataFr:
        try:
            assert(dataFr[mes].size > 0)
        except:
            raise er.NoHayDatos(mes)
        dataFr[mes] = validaTipos(dataFr[mes])
    return dataFr

# def minimo (x):
#     return min(x)

# def maximo (x):
#     return max(x)

# def positivos(lista):
#     result = [nm.array]
#     for item in lista:
#         if item > 0:
#             result.append(item)
#     return result

archivo ='finanzas2020.csv'
#archivo='finanzas2020 _NohayDatos.csv'
#archivo='finanzas2020_NumeroErroneoColumnas.csv'
#archivo = input('Escriba el nombre del archivo csv a leer: ')

try:
    assert(archivo !='')
    df = pd.read_csv(archivo, delimiter=';')
except AssertionError:
    sys.exit('No has proporcionado un nombre de archivo. Terminamos la ejecucion del programa.')
except FileNotFoundError as err:
    sys.exit(f'No existe el fichero: {archivo}. ')

# Control numero de meses
if df.columns.size != 12:
    raise er.NumeroErroneoColumnas(df.columns.size)


# Validación de si hay datos en los meses y de los tipos
df = validaSiHayDatos(df)


# Mes que se ha gastado mas
gastoMes = 0
maxGasto = 0
mesMG = [str]
for mes, valor in df.iteritems():
    if gastoMes < maxGasto:
         maxGasto = gastoMes
         mesMG = mes
    gastoMes = 0
    for item in valor:
        if item < 0:
            gastoMes += item
print("Mes en que se ha gastado más: ", mesMG, ". El gasto ha sido de : ", maxGasto," euros.")
del gastoMes
del maxGasto
del mesMG

# mes que se ha ahorrado mas (mayor diferncia entre positivo y negativo)
ingrMes = 0
maxIngr = 0
mesMI = [str]
for mes, valor in df.iteritems():
    if ingrMes > maxIngr:
        maxIngr = ingrMes
        mesMI = mes
    ingrMes = 0
    for item in valor:
            ingrMes += item
print("Mes en que se ha ahorrado más: ", mesMI, ". El valance ha sido : ",maxIngr," euros.")
del ingrMes
del maxIngr
del mesMI

# Media de gastos anuales
totalMes = 0
numFilas = 0
numMeses = 0
mediaAnual = 0
for mes, valor in df.iteritems():
    numMeses += 1
    numFilas = 0
    totalMes = 0
    for item in valor:
        numFilas += 1
        if item < 0:
            totalMes += item
    mediaAnual += totalMes/numFilas
print("La media de gasto anual ha sido: ", mediaAnual/numMeses)
del totalMes
del numFilas
del numMeses
del mediaAnual


# Gasto total anual
gasto = 0
for mes, valor in df.iteritems():
    for item in valor:
        if item < 0:
            gasto += item
print("Gasto anual: ", gasto)
del gasto

# Ingresos totales anuales
ingreso = 0
for mes, valor in df.iteritems():
    for item in valor:
        if item > 0:
            ingreso += item
print("Ingresos anuales: ", ingreso)
del ingreso



#--------------------------------------------
#Pruebas


#print(l)
# enero = positivos(df["Enero"])
# febrero = positivos(df['Febrero'])
# marzo = positivos(df['Marzo'])
# abril =  positivos(df['Abril'])
# mayo =  positivos(df['Mayo'])
# junio =  positivos(df['Junio'])
# julio =  positivos(df['Julio'])
# agosto = positivos(df['Agosto'])
# septiembre =  positivos(df['Septiembre'])
# octubre =  positivos(df['Octubre'])
# noviembre =  positivos(df['Noviembre'])
# diciembre = positivos(df['Diciembre'])

#     # Creamos uns lista con el resultado por mes
# lista = []
# # lista = {'Mes':['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'], 
#  #        'Valor':[enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre]}
# lista = {'Enero':[enero], 'Febrero':[febrero], 'Marzo':[marzo], 'Abril':[abril], 'Mayo':[mayo], 'Junio':[junio], 'Julio':[julio], 'Agosto':[agosto], 
#           'Septiembre':[septiembre], 'Octubre':[octubre], 'Noviembre':[noviembre], 'Diciembre':[diciembre]}
# meses = pd.DataFrame(lista)

# meses['Enero'].plot()



# # Mes que se ha gastado mas
# m = pd.Series()
# lp = [pd.array]
# for mes, valor in df.iteritems():
#     l = pd.Series()
#     for item in valor:
#         if item > 0:
#             keys = m.keys()
#             dato = pd.Series([item],index=[keys])
#             l = l.append(dato,ignore_index=False)
#             del dato
#             #l = l.add(añade,fill_value=0)
#             #listPos.append(item)
#     #l = l.set_index(mes)
#     #m = m.add(l,fill_values=0)
#     #meses = m.keys
#     m = m.append(l)
#     m.add(l)
#     #m = m[mes].dropna(axis=0)
#     del l   
#     #m[mes] = positivos(valor)
# año = pd.DataFrame(m)
# print(año)


# try:
#     assert(df['Enero'].size > 0)
# except:
#     raise er.NoHayDatos('Enero')
# df['Enero'] = validaTipos(df['Enero'])

# try:
#     assert(df['Febrero'].size > 0)
# except:
#     raise er.NoHayDatos('Febrero')
# df['Febrero'] = validaTipos(df['Febrero'])

# try:
#     assert(df['Marzo'].size > 0)
# except:
#     raise er.NoHayDatos('Marzo')
# df['Marzo'] = validaTipos(df['Marzo'])

# try:
#     assert(df['Abril'].size > 0)
# except:
#     raise er.NoHayDatos('Abril')
# df['Abril'] = validaTipos(df['Abril'])

# try:
#     assert(df['Mayo'].size > 0)
# except:
#     raise er.NoHayDatos('Mayo')
# df['Mayo'] = validaTipos(df['Mayo'])

# try:
#     assert(df['Junio'].size > 0)
# except:
#     raise er.NoHayDatos('Junio')
# df['Junio'] = validaTipos(df['Junio'])

# try:
#     assert(df['Julio'].size > 0)
# except:
#     raise er.NoHayDatos('Julio')
# df['Julio'] = validaTipos(df['Julio'])

# try:
#     assert(df['Agosto'].size > 0)
# except:
#     raise er.NoHayDatos('Agosto')
# df['Agosto'] = validaTipos(df['Agosto'])

# try:
#     assert(df['Septiembre'].size > 0)
# except AssertionError:
#     raise er.NoHayDatos('Septiembre')
# df['Septiembre'] = validaTipos(df['Septiembre'])

# try:
#     assert(df['Octubre'].size > 0)
# except:
#     raise er.NoHayDatos('Octubre')
# df['Octubre'] = validaTipos(df['Octubre'])

# try:
#     assert(df['Noviembre'].size > 0)
# except:
#     raise er.NoHayDatos('Noviembre')
# df['Noviembre'] = validaTipos(df['Noviembre'])

# try:
#     assert(df['Diciembre'].size > 0)
# except:
#     raise er.NoHayDatos('Diciembre')
#df['Diciembre'] = validaTipos(df['Diciembre'])

# Mes que se ha gastado mas
# enero = df.apply(positivo,df['Enero'])
# febrero = df['Febrero'].sum()
# marzo = df['Marzo'].sum()
# abril =  df['Abril'].sum()
# mayo =  df['Mayo'].sum()
# junio =  df['Junio'].sum()
# julio =  df['Julio'].sum()
# agosto = df['Agosto'].sum()
# septiembre =  df['Septiembre'].sum()
# octubre =  df['Octubre'].sum()
# noviembre =  df['Noviembre'].sum()
# diciembre = df['Diciembre'].sum()

#     # Creamos uns lista con el resultado por mes
# lista = []
# lista = {'Mes':['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'], 
#          'Valor':[enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre]}
# m = pd.DataFrame(lista)
# print(m)
# print("\n")
# print('Maximo gasto\n',m.apply(minimo,axis=0))
# print('Maximo ingreso\n',m.apply(maximo,axis=0))
# print(m.min)
# print(m.max)
# del lista
# del m

# # Media de gasto anual
# print(df.apply(nm.average, axis=0))
# list = pd.DataFrame(df.apply(nm.average, axis=0))
# print(list.apply(nm.average, axis=0))




# print(df.loc[(df['Enero'] > 0) & (df['Febrero'] > 0) & (df['Marzo'] > 0) & (df['Abril'] > 0) & (df['Mayo'] > 0) &
#     (df['Junio'] > 0) & (df['Julio'] > 0) & (df['Agosto'] > 0) & (df['Septiembre'] > 0) & (df['Octubre'] > 0) & (df['Noviembre'] > 0) & (df['Diciembre'] > 0)
# ])

# axis = 1 -> columnas
# axis = 0 -> filas
# print(min(df.sum(axis=1)))
# print(df.apply(nm.sum))

# l = df.sum(df.sum(axis=1))
# print(df.sum(axis=1))
# print(df.sum(axis=0))
# l2 = pd.crosstab(df.columns,df.columns.values)
# print(l2)

# print (df.apply(minimo,axis=1))
# print(df.apply(sum,axis=0))
# print(df.apply(sum,axis=1))

# Suponiendo que gasto sea valor negativo y ahorro valor positivo
# mes de maximo ahorro


# lista = []
# lista = {'Enero':[enero], 'Febrero':[febrero], 'Marzo':[marzo], 'Abril':[abril], 'Mayo':[mayo], 'Junio':[junio], 'Julio':[julio], 'Agosto':[agosto], 
#          'Septiembre':[septiembre], 'Octubre':[octubre], 'Noviembre':[noviembre], 'Diciembre':[diciembre]}



#m.sort_values(by=['Valores'],ascending=True)


#print(df.loc[df])

# # mes con mas gastos
# enero = df['Enero'].min()
# febrero = df['Febrero'].min()
# marzo = df['Marzo'].min()
# abril =  df['Abril'].min()
# mayo =  df['Mayo'].min()
# junio =  df['Junio'].min()
# julio =  df['Julio'].min()
# agosto = df['Agosto'].min()
# septiembre =  df['Septiembre'].min()
# octubre =  df['Octubre'].min()
# noviembre =  df['Noviembre'].min()
# diciembre = df['Diciembre'].min()
# lista = []
# lista = {'Enero':[enero], 'Febrero':[febrero], 'Marzo':[marzo], 'Abril':[abril], 'Mayo':[mayo], 'Junio':[junio], 'Julio':[julio], 'Agosto':[agosto], 
#         'Septiembre':[septiembre], 'Octubre':[octubre], 'Noviembre':[noviembre], 'Diciembre':[diciembre]}
# m = pd.DataFrame(lista)

# print(nm.min(m,axis=1))
# print(m.min)
# del lista
