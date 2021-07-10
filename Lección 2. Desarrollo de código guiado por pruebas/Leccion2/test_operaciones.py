import pytest
import operaciones

def test_suma():
    x = 5
    y = 5
    resultado = 10
    assert resultado == operaciones.suma(x,y)

def test_resta():
    x = 8
    y = 8
    resultado = 0
    assert resultado == operaciones.resta(x,y)

def test_division():
    x = 10
    y = 2
    resultado = 5
    assert resultado == operaciones.division(x,y)

def test_operacion_inventada():
    assert operaciones.operacion_inventada(6,0,12) == 0

def test_minimo():
    assert operaciones.minimo([2,3,-1,8,88,57,-23]) == -23

def test_es_primo():
    assert operaciones.es_primo(8)==False
    assert operaciones.es_primo(5)==True