import pytest
from clases import Participante, Taller

def test_es_mayor_edad():
    p1 = Participante("Ana", 20, "ana10@mail.com")
    p2 = Participante("Luis", 16, "luis8@mail.com")
    assert p1.es_mayor_edad() is True
    assert p2.es_mayor_edad() is False

# cupos disponibles

# inscripciones
