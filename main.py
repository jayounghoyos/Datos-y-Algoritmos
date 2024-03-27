import random
import csv  # Necesario para leer archivos CSV


# Colores ANSI
class colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Cola:
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
        nodo_actual = self.primero
        while nodo_actual:
            estudiante = nodo_actual.valor
            print(
                f"Nombre: {estudiante.nombre}, ID: {estudiante.id}, Perfil: {estudiante.categoria}, Prioridad: {estudiante.prioridad}, Créditos: {estudiante.creditos}")
            nodo_actual = nodo_actual.siguiente


class Estudiante:
    def __init__(self, nombre, id, categoria, prioridad):
        self.nombre = nombre
        self.id = id
        self.categoria = categoria
        self.prioridad = prioridad
        self.creditos = 5

    def __repr__(self):
        return f"{self.nombre}, ID: {self.id}, Categoría: {self.categoria}, Prioridad: {self.prioridad}, Créditos: {self.creditos}"


def leer_estudiantes_csv(archivo):
    estudiantes = []
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)  # Saltar cabecera
        for fila in lector:
            nombre, id, categoria, prioridad = fila
            estudiantes.append(Estudiante(nombre, id, categoria, int(prioridad)))
    return estudiantes


def main():
    dataset = "dataset.csv"  # Asegúrate de tener este archivo en tu directorio de trabajo
    estudiantes = leer_estudiantes_csv(dataset)

    # Selecciona una muestra aleatoria de estudiantes
    tamaño_muestra = random.randint(1, 10)
    muestra_estudiantes = random.sample(estudiantes, tamaño_muestra)

    # Organiza los estudiantes en la muestra por prioridad y los encola
    parqueadero = Cola()
    for estudiante in sorted(muestra_estudiantes, key=lambda est: est.prioridad, reverse=True):
        parqueadero.encolar(estudiante)

    # Muestra los estudiantes encolados en el parqueadero
    parqueadero.imprimir()


if __name__ == "__main__":
    main()
