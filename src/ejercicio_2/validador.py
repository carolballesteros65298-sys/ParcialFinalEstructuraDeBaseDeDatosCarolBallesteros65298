from collections import deque


def validar_traza(acciones):
    cola = deque(acciones)
    pila = []

    while cola:
        accion = cola.popleft()

        if accion.startswith("ABRIR_PREGUNTA"):
            numero = int(accion.split("(")[1].rstrip(")"))
            pila.append(numero)

        elif accion.startswith("RESPONDER"):
            numero = int(accion.split("(")[1].rstrip(")"))
            if not pila:
                return f"Invalida: se intento responder la pregunta {numero} sin ninguna pregunta abierta"
            if pila[-1] != numero:
                return f"Invalida: se intento responder la pregunta {numero} pero el contexto activo es la pregunta {pila[-1]}"

        elif accion.startswith("GUARDAR"):
            numero = int(accion.split("(")[1].rstrip(")"))
            if not pila or pila[-1] != numero:
                contexto = pila[-1] if pila else "ninguno"
                return f"Invalida: se intento guardar la pregunta {numero} pero el contexto activo es {contexto}"

        elif accion == "VOLVER":
            if not pila:
                return "Invalida: se ejecuto VOLVER sin ninguna pregunta abierta en el contexto"
            pila.pop()

        elif accion == "ENVIAR":
            if pila:
                return f"Invalida: se intento enviar con preguntas aun abiertas en el contexto: {pila}"
            return "Valida"

    return "Valida"


if __name__ == "__main__":
    print("Caso normal - traza valida completa:")
    traza_valida = [
        "ABRIR_PREGUNTA(1)",
        "RESPONDER(1)",
        "GUARDAR(1)",
        "VOLVER",
        "ABRIR_PREGUNTA(2)",
        "RESPONDER(2)",
        "GUARDAR(2)",
        "VOLVER",
        "ENVIAR"
    ]
    print(validar_traza(traza_valida))

    print("\nCaso limite - responder una pregunta que no esta activa:")
    traza_contexto_incorrecto = [
        "ABRIR_PREGUNTA(1)",
        "RESPONDER(2)",
    ]
    print(validar_traza(traza_contexto_incorrecto))

    print("\nCaso de error potencial - VOLVER sin nada en la pila:")
    traza_volver_vacia = [
        "VOLVER"
    ]
    print(validar_traza(traza_volver_vacia))

    print("\nCaso de error potencial - ENVIAR con preguntas aun abiertas:")
    traza_enviar_abierto = [
        "ABRIR_PREGUNTA(1)",
        "RESPONDER(1)",
        "ENVIAR"
    ]
    print(validar_traza(traza_enviar_abierto))
