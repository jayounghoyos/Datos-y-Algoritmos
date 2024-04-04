import random  # aleatoriedad
import pandas as pd  # Necesario para leer archivos CSV con pandas, se le usará como pd


# Colores ANSI
class colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


# la clase nodo cuenta con un constructor que contiene un parametro (valor) que representa los datos guardados en el nodo
class Node:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    # self.sifguiente inicia con valor nulo, es decir, no se apunta a ningún otro nodo


class Pila:  # sirve para crear el historial de los créditos ingresados

    def __init__(self):  # se crea un constructor que genera una lista vacía
        self.items = []

        # se crean los métodos para la pila

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def imprimir(self):
        if self.esta_vacia():
            print("La pila está vacía.")
        else:
            # Se le hizo reversed para que se vea como un historial
            for elemento in reversed(self.items):
                print(elemento)


class Cola:

    # Constructor de la lista enlazada primero(head) y último(tail))
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def encolar(self, elemento):
        nuevo_nodo = Node(elemento)
        if self.ultimo:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
        if not self.primero:
            self.primero = nuevo_nodo

    def desencolar(self):
        if self.primero:
            valor_retirado = self.primero.valor
            self.primero = self.primero.siguiente
            if not self.primero:
                self.ultimo = None
            return valor_retirado
        return None

    def esta_vacia(self):
        return self.primero is None

    def imprimir(self):
        print(colors.YELLOW + "Contenido de la cola:" + colors.RESET)
        nodo_actual = self.primero
        while nodo_actual:
            estudiante = nodo_actual.valor
            print(
                f"Nombre: {estudiante.nombre}, ID: {estudiante.id}, Perfil: {estudiante.categoria}, Prioridad: {estudiante.prioridad}, Créditos: {estudiante.creditos}"
            )
            nodo_actual = nodo_actual.siguiente

    def restar_creditos(self):
        nodo_actual = self.primero
        nodo_anterior = None  # Un registro del nodo anterior para poder desencolar al estudiante sin créditos
        # Restar un crédito al estudiante cada día hasta que no tenga créditos.
        # Si tiene 0 créditos, imprimir expulsión.
        # Si el nodo anterior no está vacío, actualizar primero.
        # Si se remueve el último nodo, actualizar último.
        while nodo_actual:
            estudiante = nodo_actual.valor
            if estudiante.creditos > 0:
                nodo_actual.valor.creditos -= 1
                if estudiante.creditos == 0:
                    print("\n" + colors.CYAN + estudiante.nombre,
                          "Ya no puedes ingresar" + colors.RESET + "\n")
                    # Desencolar al estudiante actual
                    if nodo_anterior is not None:
                        nodo_anterior.siguiente = nodo_actual.siguiente
                        if nodo_actual == self.ultimo:
                            self.ultimo = nodo_anterior
                    else:
                        self.primero = nodo_actual.siguiente
                        if nodo_actual == self.ultimo:
                            self.ultimo = None
                # Sale del bucle una vez que el estudiante sin créditos ha sido desencolado
                elif estudiante.creditos <= 1:
                    print("\n" + colors.BLUE + estudiante.nombre,
                          "Tiene que recargar" + colors.RESET + "\n")

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

    def agregar_creditos(self, id, cantidad):
        nodo_actual = self.primero  # para empezar con el primer nodo
        estudiante_encontrado = False  # se inicializa como no encontrado
        while nodo_actual:
            estudiante = nodo_actual.valor  # estudiante será igual a los valores de los nodos por cada iteración
            if estudiante.id == id:
                estudiante.creditos += cantidad  # se le suma la cantidad de créditos ingresados
                print(
                    colors.BLUE +
                    f"Se han añadido {cantidad} créditos a {estudiante.nombre}. Créditos actuales: {estudiante.creditos}"
                    + colors.RESET)  # uso de format para organizar el texto UwU
                estudiante_encontrado = True
                break
            nodo_actual = nodo_actual.siguiente
        if not estudiante_encontrado:
            print(f"Estudiante con ID {id} no encontrado en el parqueadero.")

    def encolar_estudiante(self, nombre, id, categoria, prioridad):
        nuevo_estudiante = Estudiante(nombre, id, categoria, prioridad)
        self.encolar(nuevo_estudiante)

    def organizar_por_prioridad(self):
        # Crear una lista de estudiantes a partir de los elementos de la cola
        estudiantes = []
        nodo_actual = self.primero
        while nodo_actual:
            estudiantes.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

        # Ordenar la lista de estudiantes por prioridad
        estudiantes_ordenados = sorted(estudiantes, key=lambda est: est.prioridad, reverse=True)

        # Limpiar la cola
        self.primero = None
        self.ultimo = None

        # Volver a encolar los estudiantes en la cola ordenada
        for estudiante in estudiantes_ordenados:
            self.encolar(estudiante)

    def desencolar_estudiante_por_id(self, id_estudiante):
        nodo_actual = self.primero
        nodo_anterior = None

        while nodo_actual:
            estudiante = nodo_actual.valor
            if estudiante.id == id_estudiante:
                estudiante_desencolado = estudiante
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    if not nodo_actual.siguiente:
                        self.ultimo = nodo_anterior
                else:
                    self.primero = nodo_actual.siguiente
                    if not nodo_actual.siguiente:
                        self.ultimo = None
                return estudiante_desencolado

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        print(colors.RED + f"Estudiante con ID {id_estudiante} no encontrado en el parqueadero." + colors.RESET)
        return None


class Estudiante:
    # Constructor del estudiante
    def __init__(self, nombre, id, categoria, prioridad):
        self.nombre = nombre
        self.id = id
        self.categoria = categoria
        self.prioridad = prioridad
        self.creditos = random.randint(5, 8)  # Minimo 5 cumpliendo el requerimiento.


def leer_estudiantes_csv(archivo):
    # Pandas(pd) para leer el archivo CSV
    df = pd.read_csv(archivo)
    estudiantes = [Estudiante(row['Nombre'], int(row['ID']), row['Categoria'], int(row['Prioridad'])) for index, row in
                   df.iterrows()]
    return estudiantes


def main():
    dataset = "dataset.csv"
    estudiantes = leer_estudiantes_csv(dataset)

    # Selecciona una muestra aleatoria de estudiantes
    tamaño_muestra = random.randint(1, 10)
    muestra_estudiantes = random.sample(estudiantes, tamaño_muestra)

    # Organiza los estudiantes en la muestra por prioridad y los encola
    parqueadero = Cola()
    estudiantes_ordenados = sorted(muestra_estudiantes, key=lambda est: est.prioridad, reverse=True)
    for estudiante in estudiantes_ordenados:
        parqueadero.encolar(estudiante)

    parqueadero.imprimir()

    credit_history = Pila()  # el historial de créditos como pila

    menu = True
    while menu:
        print(" ")
        print(colors.MAGENTA + "¡Este es el menu del parqueadero!")
        print("1) Agregar Creditos")
        print(
            "2) Pasó un día en el parqueadero, se restan los créditos de los estudiantes")  # Opción del desarrollador de que pase un día y reste creditos
        print("3) Historial de creditos")
        print("4) Imprimir estudiantes en el parqueadero")
        print("5) Ingresar estudiante al parqueadero")
        print("6) Quiero salir del parqueadero")
        print("7) Salir")
        opcion = int(input("\nDigita la opción del menu: " + colors.RESET))
        print(" ")

        if opcion == 1:
            id = int(input("Digita el ID del estudiante: "))
            cantidad = int(input("Digita la cantidad de creditos a agregar: "))
            parqueadero.agregar_creditos(id, cantidad)
            credit_history.apilar(f"Se han añadido {cantidad} créditos a {id}")
        elif opcion == 2:
            print(colors.RED + "Ha pasado un día en el parqueadero se le restó 1 credito a las personas" + colors.RESET)
            parqueadero.restar_creditos()
            parqueadero.imprimir()
        elif opcion == 3:
            print(colors.YELLOW + "Historial de creditos" + colors.RESET)
            credit_history.imprimir()
        elif opcion == 4:
            parqueadero.imprimir()

        elif opcion == 5:
            print("Digita los datos del estudiante de la siguiente manera -> (Nombre, ID, Categoria, Prioridad)")
            nombre = input("Nombre: ")
            id = int(input("ID: "))
            categoria = input("Categoria: ").lower()
            prioridad = 0
            if categoria == "honor" or categoria == "ecologico":
                prioridad = 1
            parqueadero.encolar_estudiante(nombre, id, categoria, prioridad)
            parqueadero.organizar_por_prioridad()
            parqueadero.imprimir()

        elif opcion == 6:
            id_estudiante_desencolar = int(
                input("Digite el ID del estudiante que desea desencolar: "))
            estudiante_desencolado = parqueadero.desencolar_estudiante_por_id(id_estudiante_desencolar)
            if estudiante_desencolado:
                print(f"Estudiante {estudiante_desencolado.nombre} desencolado correctamente.")
        elif opcion == 7:
            break
        else:
            print("Digita una opción válida.")
    print("¡Gracias por usar el parqueadero!")


if __name__ == "__main__":
    main()