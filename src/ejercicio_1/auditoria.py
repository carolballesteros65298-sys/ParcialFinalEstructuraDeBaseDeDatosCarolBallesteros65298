class Solicitud:
    def __init__(self, id, codigo, tipo, prioridad, fecha, estado):
        self.id = id
        self.codigo = codigo
        self.tipo = tipo
        self.prioridad = prioridad
        self.fecha = fecha
        self.estado = estado

    def __repr__(self):
        return f"[{self.id}, {self.codigo}, {self.tipo}, {self.prioridad}, {self.fecha}, {self.estado}]"


def insertar(lista, solicitud):
    lista.append(solicitud)


def eliminar_duplicados(lista):
    vistos = set()
    sin_duplicados = []
    for s in lista:
        if s.id not in vistos:
            sin_duplicados.append(s)
            vistos.add(s.id)
    return sin_duplicados


def eliminar_canceladas(lista):
    return [s for s in lista if s.estado != "cancelada"]


def mover_alta_prioridad(lista):
    altas = [s for s in lista if s.prioridad == "alta"]
    otras = [s for s in lista if s.prioridad != "alta"]
    return altas + otras


def depurar(lista):
    lista = eliminar_duplicados(lista)
    lista = eliminar_canceladas(lista)
    lista = mover_alta_prioridad(lista)
    return lista


if __name__ == "__main__":
    solicitudes = []

    insertar(solicitudes, Solicitud(101, 20241001, "homologacion", "media", "2026-06-01", "activa"))
    insertar(solicitudes, Solicitud(102, 20241002, "cancelacion", "alta", "2026-06-01", "activa"))
    insertar(solicitudes, Solicitud(101, 20241001, "homologacion", "media", "2026-06-01", "activa"))
    insertar(solicitudes, Solicitud(103, 20241003, "supletorio", "alta", "2026-06-02", "cancelada"))
    insertar(solicitudes, Solicitud(104, 20241004, "reingreso", "baja", "2026-06-02", "activa"))
    insertar(solicitudes, Solicitud(105, 20241005, "validacion", "alta", "2026-06-03", "activa"))

    print("Caso normal - lista completa con duplicados, canceladas y prioridades mezcladas:")
    resultado = depurar(solicitudes)
    for s in resultado:
        print(s)

    print("\nCaso limite - lista con un solo elemento:")
    unica = [Solicitud(200, 20241010, "reingreso", "alta", "2026-06-03", "activa")]
    for s in depurar(unica):
        print(s)

    print("\nCaso de error potencial - lista vacia:")
    vacia = []
    resultado_vacio = depurar(vacia)
    print(resultado_vacio if resultado_vacio else "Lista vacia: no hay solicitudes para procesar")
