import pytest
import pandas
import activ_1

def test_ValidaTipos():
    listx = [1,-3,'bug',2000,'074',"ERROR",10,3,-3,'-34']
    resultado = [1,-3,0,2000,74,0,10,3,-3,-34]
    assert resultado == activ_1.validaTipos(listx)

def test_ValidaSiHayDatos():
    l = {'Enero':[1],'Febrero':[1],
         'Marzo':[1],
         'Abril':[1],'Mayo':[1],
         'Junio':[1],'Julio':[1],
         'Agosto':[1],'Septiembre':[1],
         'Octubre':[1],'Noviembre':[1],
         'Diciembre':[1]}
    df = pandas.DataFrame(l)
    l2 = {'Enero':[1],'Febrero':[1],
          'Marzo':[1],
          'Abril':[1],'Mayo':[1],
          'Junio':[1],'Julio':[1],
          'Agosto':[1],'Septiembre':[1],
          'Octubre':[1],'Noviembre':[1],
          'Diciembre':[1]}
    resultado = pandas.DataFrame(l2)
    df2 = activ_1.validaSiHayDatos(df)
    for item,valores in df2.iteritems():
            assert resultado[item].size == df2[item].size