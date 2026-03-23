from clases import Participante, Taller, SistemaReservas

def test_pago_falla_no_registra():
    sistema = SistemaReservas()
    taller = Taller("Yoga", 10)
    sistema.agregar_taller(taller)

    participante = Participante("Asier", 20, "a@a.com")

    resultado = sistema.registrar_participante_en_taller(taller, participante, monto=0)

    assert resultado is False
    assert participante not in taller.lista_inscritos


def test_pago_exitoso_registra():
    sistema = SistemaReservas()
    taller = Taller("Yoga", 10)
    sistema.agregar_taller(taller)

    participante = Participante("Asier", 20, "a@a.com")

    resultado = sistema.registrar_participante_en_taller(taller, participante, monto=10)

    assert resultado is True
    assert participante in taller.lista_inscritos
