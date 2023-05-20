from datetime import datetime

# Clase para representar un punto geografico
class PuntoGeografico:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


# Clase para representar un turno de recoleccion
class TurnoRecoleccion:
    def __init__(self, camion, conductor, asistentes, ruta, hora_inicio, hora_fin):
        self.camion = camion
        self.conductor = conductor
        self.asistentes = asistentes
        self.ruta = ruta
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.localizacion = None
        self.carga = {'vidrio': 0, 'papel': 0, 'plastico': 0, 'metal': 0, 'organicos': 0}

    def registrar_localizacion(self, localizacion):
        self.localizacion = localizacion

    def agregar_carga(self, tipo_residuo, cantidad):
        self.carga[tipo_residuo] += cantidad

    def obtener_carga_vidrio(self):
        return self.carga['vidrio']


# Clase para representar un camion
class Camion:
    def __init__(self, identificacion):
        self.identificacion = identificacion


# Clase para representar una persona
class Persona:
    def __init__(self, identificacion):
        self.identificacion = identificacion


# Clase para administrar la operacion de TrashCity
class TrashCity:
    def __init__(self):
        self.turnos = []

    def agregar_turno_recoleccion(self, turno):
        self.turnos.append(turno)

    def obtener_cantidad_vidrio_por_dia(self, fecha):
        cantidad_vidrio = 0
        for turno in self.turnos:
            if turno.hora_inicio.date() == fecha:
                cantidad_vidrio += turno.obtener_carga_vidrio()
        return cantidad_vidrio


# Pruebas unitarias
def test_trash_city():
    # Crear objetos
    camion = Camion("ABC123")
    conductor = Persona("123456789")
    asistente1 = Persona("987654321")
    asistente2 = Persona("456789123")
    ruta = [PuntoGeografico(1.234, 5.678), PuntoGeografico(9.876, 5.432)]
    hora_inicio = datetime(2023, 5, 19, 8, 0)
    hora_fin = datetime(2023, 5, 19, 12, 0)

    # Crear turno de recoleccion
    turno = TurnoRecoleccion(camion, conductor, [asistente1, asistente2], ruta, hora_inicio, hora_fin)

    # Registrar localizacion y agregar carga
    localizacion = PuntoGeografico(1.111, 2.222)
    turno.registrar_localizacion(localizacion)
    turno.agregar_carga('vidrio', 2)
    turno.agregar_carga('papel', 1)
    turno.agregar_carga('plastico', 3)
    turno.agregar_carga('metal', 1.5)
    turno.agregar_carga('organicos', 2.5)

    # Crear instancia de TrashCity y agregar turno
    trash_city = TrashCity()
    trash_city.agregar_turno_recoleccion(turno)

    # Verificar la cantidad de vidrio recolectado en la fecha dada
    fecha = datetime(2023, 5, 19).date()
    cantidad_vidrio = trash_city.obtener_cantidad_vidrio_por_dia(fecha)
    assert cantidad_vidrio == 2


# Ejecutar pruebas unitarias
test_trash_city()
