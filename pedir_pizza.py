import time

# Datos iniciales
MASAS = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
SALSAS = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
INGREDIENTES = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

# Funciones
def mostrar_menu_principal():
    print("\n--- Menú de Personalización de Pizza ---")
    print("1. Elegir tipo de masa")
    print("2. Elegir tipo de salsa")
    print("3. Agregar ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Mostrar ingredientes actuales")
    print("6. Confirmar y calcular tiempo")
    print("7. Salir")

def elegir_opcion():
    while True:
        try:
            opcion = int(input("Elija una opción (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

def elegir_masa():
    print("\n--- Elija el tipo de masa ---")
    for i, masa in enumerate(MASAS):
        print(f"{i + 1}. {masa}")
    while True:
        try:
            opcion = int(input("Ingrese el número de su elección: "))
            if 1 <= opcion <= len(MASAS):
                return MASAS[opcion - 1]
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

def elegir_salsa():
    print("\n--- Elija el tipo de salsa ---")
    for i, salsa in enumerate(SALSAS):
        print(f"{i + 1}. {salsa}")
    while True:
        try:
            opcion = int(input("Ingrese el número de su elección: "))
            if 1 <= opcion <= len(SALSAS):
                return SALSAS[opcion - 1]
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

def manejar_ingredientes(ingredientes_actuales):
    print("\n--- Ingredientes disponibles ---")
    for i, ingrediente in enumerate(INGREDIENTES):
        print(f"{i + 1}. {ingrediente}")

    print("\n1. Agregar ingrediente")
    print("2. Eliminar ingrediente")
    print("3. Volver al menú principal")
    while True:
        try:
            opcion = int(input("Elija una opción (1-3): "))
            if opcion == 1:
                ingrediente = elegir_ingrediente(INGREDIENTES)
                if ingrediente not in ingredientes_actuales:
                    ingredientes_actuales.append(ingrediente)
                else:
                    print("El ingrediente ya está en la pizza.")
            elif opcion == 2:
                ingrediente = elegir_ingrediente(ingredientes_actuales)
                if ingrediente in ingredientes_actuales:
                    ingredientes_actuales.remove(ingrediente)
                else:
                    print("El ingrediente no está en la pizza.")
            elif opcion == 3:
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

def elegir_ingrediente(opciones):
    print("\n--- Elija un ingrediente ---")
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    while True:
        try:
            opcion = int(input("Ingrese el número de su elección: "))
            if 1 <= opcion <= len(opciones):
                return opciones[opcion - 1]
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

def calcular_tiempo(ingredientes):
    tiempo_base = 20
    tiempo_adicional = len(ingredientes) * 2
    return tiempo_base + tiempo_adicional

def mostrar_ingredientes(ingredientes):
    print("\n--- Ingredientes actuales en la pizza ---")
    if ingredientes:
        for ingrediente in ingredientes:
            print(f"- {ingrediente}")
    else:
        print("No hay ingredientes en la pizza.")

def main():
    masa = None
    salsa = None
    ingredientes = []

    while True:
        mostrar_menu_principal()
        opcion = elegir_opcion()

        if opcion == 1:
            masa = elegir_masa()
            print(f"Tipo de masa seleccionado: {masa}")
        elif opcion == 2:
            salsa = elegir_salsa()
            print(f"Tipo de salsa seleccionado: {salsa}")
        elif opcion == 3 or opcion == 4:
            manejar_ingredientes(ingredientes)
        elif opcion == 5:
            mostrar_ingredientes(ingredientes)
        elif opcion == 6:
            if masa and salsa:
                tiempo = calcular_tiempo(ingredientes)
                print(f"\nSu pizza estará lista en {tiempo} minutos.")
                confirmar = input("¿Desea confirmar el pedido? (sí/no): ").strip().lower()
                if confirmar == 'sí':
                    print("¡Pedido confirmado! Su pizza está en proceso.")
                    break
                else:
                    print("Pedido cancelado.")
            else:
                print("Debe seleccionar la masa y la salsa antes de confirmar.")
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
