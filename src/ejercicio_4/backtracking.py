def es_asignacion_valida(evaluacion, sala, asignaciones_actuales):
    if evaluacion["estudiantes"] > sala["capacidad"]:
        return False

    if evaluacion["horario"] not in sala["horarios"]:
        return False

    if evaluacion["computador"] and not sala["computador"]:
        return False

    for asignacion in asignaciones_actuales:
        if asignacion["sala"] == sala["codigo"] and asignacion["horario"] == evaluacion["horario"]:
            return False

    return True


def backtracking(evaluaciones, salas, asignaciones=None):
    if asignaciones is None:
        asignaciones = []

    if len(asignaciones) == len(evaluaciones):
        return asignaciones

    indice = len(asignaciones)
    evaluacion_actual = evaluaciones[indice]

    for sala in salas:
        if es_asignacion_valida(evaluacion_actual, sala, asignaciones):
            asignaciones.append({
                "evaluacion": evaluacion_actual["codigo"],
                "sala": sala["codigo"],
                "horario": evaluacion_actual["horario"]
            })
            resultado = backtracking(evaluaciones, salas, asignaciones)
            if resultado is not None:
                return resultado
            asignaciones.pop()

    return None


if __name__ == "__main__":
    print("Caso normal - asignacion posible con restricciones:")
    evaluaciones = [
        {"codigo": "EDA",  "estudiantes": 30, "horario": "18:00-20:00", "computador": True},
        {"codigo": "BD",   "estudiantes": 25, "horario": "18:00-20:00", "computador": True},
        {"codigo": "CALC", "estudiantes": 40, "horario": "20:00-22:00", "computador": False},
    ]
    salas = [
        {"codigo": "A101", "capacidad": 35, "horarios": ["18:00-20:00", "20:00-22:00"], "computador": True},
        {"codigo": "A102", "capacidad": 30, "horarios": ["18:00-20:00"],                "computador": True},
        {"codigo": "B201", "capacidad": 50, "horarios": ["20:00-22:00"],                "computador": False},
    ]
    resultado = backtracking(evaluaciones, salas)
    if resultado:
        print("Asignacion encontrada:")
        for a in resultado:
            print(f"  Evaluacion {a['evaluacion']} en sala {a['sala']} a las {a['horario']}")
    else:
        print("No se encontro una asignacion valida.")

    print("\nCaso limite - una sola evaluacion y una sola sala valida:")
    ev_unica = [{"codigo": "MAT", "estudiantes": 20, "horario": "08:00-10:00", "computador": False}]
    sala_unica = [{"codigo": "C101", "capacidad": 25, "horarios": ["08:00-10:00"], "computador": False}]
    resultado2 = backtracking(ev_unica, sala_unica)
    print("Resultado:", resultado2)

    print("\nCaso sin solucion - evaluacion requiere computador pero ninguna sala disponible lo tiene:")
    ev_sin_solucion = [{"codigo": "PRG", "estudiantes": 10, "horario": "10:00-12:00", "computador": True}]
    salas_sin_pc = [{"codigo": "D201", "capacidad": 30, "horarios": ["10:00-12:00"], "computador": False}]
    resultado3 = backtracking(ev_sin_solucion, salas_sin_pc)
    print("Resultado:", resultado3 if resultado3 else "No hay solucion valida para esta configuracion")
