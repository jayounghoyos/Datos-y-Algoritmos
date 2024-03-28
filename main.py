import random
import pandas as pd  # Necesario para leer archivos CSV con pandas, se le usará como pd


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


class Pila:

  def __init__(self):
    self.items = []

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
      #Se le hizo reversed para que se vea como un historia tipico con lo más reciente arriba
      for elemento in reversed(self.items):
        print(elemento)


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
    while nodo_actual:
      estudiante = nodo_actual.valor
      if estudiante.creditos > 0:
        nodo_actual.valor.creditos -= 1

        if estudiante.creditos <= 1:
          print(colors.RED + estudiante.nombre, "Tiene que recargar" + colors.RESET)
      nodo_actual = nodo_actual.siguiente

  def agregar_creditos(self, id, cantidad):
    nodo_actual = self.primero
    estudiante_encontrado = False
    while nodo_actual:
      estudiante = nodo_actual.valor
      print(f"Revisando estudiante con ID {estudiante.id}")
      if estudiante.id == id:
        estudiante.creditos += cantidad
        print(
            colors.BLUE +
            f"Se han añadido {cantidad} créditos a {estudiante.nombre}. Créditos actuales: {estudiante.creditos}"
            + colors.RESET)
        estudiante_encontrado = True
        break
      nodo_actual = nodo_actual.siguiente
    if not estudiante_encontrado:
      print(f"Estudiante con ID {id} no encontrado en el parqueadero.")


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
  #Pandas(pd) para leer el archivo CSV
  df = pd.read_csv(archivo)

  estudiantes = [
      Estudiante(row['Nombre'], int(row['ID']), row['Categoria'],
                 int(row['Prioridad'])) for index, row in df.iterrows()
  ]

  return estudiantes


def main():
  dataset = "dataset.csv"
  estudiantes = leer_estudiantes_csv(dataset)

  # Selecciona una muestra aleatoria de estudiantes
  tamaño_muestra = random.randint(1, 10)
  muestra_estudiantes = random.sample(estudiantes, tamaño_muestra)

  # Organiza los estudiantes en la muestra por prioridad y los encola
  parqueadero = Cola()
  for estudiante in sorted(muestra_estudiantes,
                           key=lambda est: est.prioridad,
                           reverse=True):
    parqueadero.encolar(estudiante)

  # Muestra los estudiantes encolados en el parqueadero
  parqueadero.imprimir()

  credit_history = Pila()

  menu = True
  while menu:
    print(colors.MAGENTA + "¡Este es el menu del parqueadero!")
    print("1) Agregar Creditos")
    print(
        "2) Pasó un día en el parqueadero"
    )  #Opción del desarrollador de que pase un día y cambien los creditos
    print("3) Historial de creditos")
    print("4) Salir")
    opcion = int(input("Digita la opción del menu: " + colors.RESET))

    if opcion == 1:
      id = int(input("Digita el ID del estudiante: "))
      cantidad = int(input("Digita la cantidad de creditos a agregar: "))
      parqueadero.agregar_creditos(id, cantidad)
      credit_history.apilar(f"Se han añadido {cantidad} créditos a {id}")
    elif opcion == 2:
      print(
          colors.RED +
          "Ha pasado un día en el parqueadero se le restó 1 credito a las personas"
          + colors.RESET)
      parqueadero.restar_creditos()
      parqueadero.imprimir()
    elif opcion == 3:
      print(colors.YELLOW + "Historial de creditos" + colors.RESET)
      credit_history.imprimir()

    elif opcion == 4:
      break
    else:
      print("Digita una opción válida.")
  print("¡Gracias por usar el parqueadero!")


if __name__ == "__main__":
  main()
