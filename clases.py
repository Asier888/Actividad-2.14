class Participante:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def es_mayor_edad(self):
        return self.edad >= 18


class Taller:
    def __init__(self, nombre, limite_asistentes):
        self.nombre = nombre
        self.limite_asistentes = limite_asistentes
        self.lista_inscritos = []

    def cupos_disponibles(self):
        return self.limite_asistentes - len(self.lista_inscritos)

    def inscribir_participante(self, participante):
        if participante.es_mayor_edad() and self.cupos_disponibles() > 0:
            self.lista_inscritos.append(participante)
            return True
        return False


class SistemaReservas:
    def __init__(self):
        self.talleres = []

    def agregar_taller(self, taller):
        self.talleres.append(taller)

    def registrar_participante_en_taller(self, taller, participante, monto):
        # 1. Comprobar pago
        if not procesar_pago(participante, monto):
            return False

        # 2. Intentar inscribir en el taller
        return taller.inscribir_participante(participante)

    def listar_participantes_taller(self, taller):
        return [p.nombre for p in taller.lista_inscritos]


def procesar_pago(participante, monto):
    """
    Simula un pago. Devuelve True si el pago es exitoso,
    False si falla.
    """
    return monto > 0

