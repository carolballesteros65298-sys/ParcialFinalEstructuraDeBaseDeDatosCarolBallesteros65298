class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)


def contar_actividades(nodo):
    if not nodo.hijos:
        return 1 if "Actividad" in nodo.nombre else 0
    return sum(contar_actividades(hijo) for hijo in nodo.hijos)


def profundidad(nodo):
    if not nodo.hijos:
        return 1
    return 1 + max(profundidad(hijo) for hijo in nodo.hijos)


def buscar(nodo, nombre):
    if nodo.nombre == nombre:
        return True
    return any(buscar(hijo, nombre) for hijo in nodo.hijos)


def imprimir_arbol(nodo, nivel=0):
    print("  " * nivel + nodo.nombre)
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)


def construir_arbol_ejemplo():
    programa = Nodo("Programa")

    materia1 = Nodo("Estructuras de Datos")
    unidad1 = Nodo("Unidad 1")
    unidad1.agregar_hijo(Nodo("Actividad: Listas"))
    unidad1.agregar_hijo(Nodo("Quiz 1"))
    unidad2 = Nodo("Unidad 2")
    unidad2.agregar_hijo(Nodo("Actividad: Pilas y Colas"))
    materia1.agregar_hijo(unidad1)
    materia1.agregar_hijo(unidad2)

    materia2 = Nodo("Algoritmos")
    unidad3 = Nodo("Unidad 1")
    unidad3.agregar_hijo(Nodo("Actividad: Recursividad"))
    materia2.agregar_hijo(unidad3)

    programa.agregar_hijo(materia1)
    programa.agregar_hijo(materia2)
    return programa


if __name__ == "__main__":
    arbol = construir_arbol_ejemplo()

    print("Caso normal - estructura completa del arbol:")
    imprimir_arbol(arbol)

    print(f"\nTotal de actividades: {contar_actividades(arbol)}")
    print(f"Profundidad maxima: {profundidad(arbol)}")
    print(f"Buscar 'Quiz 1': {buscar(arbol, 'Quiz 1')}")
    print(f"Buscar 'Examen Final': {buscar(arbol, 'Examen Final')}")

    print("\nCaso limite - arbol de un solo nodo:")
    nodo_solo = Nodo("Actividad: Unica")
    print(f"Actividades: {contar_actividades(nodo_solo)}")
    print(f"Profundidad: {profundidad(nodo_solo)}")

    print("\nCaso de error potencial - nodo sin hijos que no es actividad:")
    nodo_vacio = Nodo("Materia sin contenido")
    print(f"Actividades: {contar_actividades(nodo_vacio)}")
