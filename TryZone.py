import random


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
    print(colors.YELLOW + "Contenido de la pila:" + colors.RESET)
    for elemento in self.items:
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
    else:
      return None

  def esta_vacia(self):
    return self.primero is None

  def imprimir(self):
    print(colors.BLUE + "La cola tiene: " + colors.RESET)
    nodo_actual = self.primero
    while nodo_actual:
      print(nodo_actual)
      nodo_actual = nodo_actual.siguiente


class Estudiante:
  creditos = 5

  def __init__(self, nombre, id, categoria, prioridad):
    self.nombre = nombre
    self.id = id
    self.categoria = categoria
    self.creditos = 5
    self.prioridad = prioridad

  def recargar_creditos(self, num_creditos):
    self.creditos += num_creditos


def obtener_lista_csv(archivo):
  parqueadero = []
  with open(archivo) as archivo_csv:
    next(archivo_csv)  # Saltar la primera línea (cabecera)
    for linea in archivo_csv:
      linea = linea.strip("\n")
      columnas = linea.split(",")
      nombre = columnas[0]
      id = int(columnas[1])
      perfil = columnas[2]
      Prioridad = int(columnas[3])
      parqueadero.append({
          "nombre": nombre,
          "id": id,
          "perfil": perfil,
          "Prioridad": Prioridad
      })
  return parqueadero


def generar_lista_aleatoria_desde_csv(archivo, tamaño):
  lista = []
  datos_csv = obtener_lista_csv(archivo)
  for _ in range(tamaño):
    # Seleccionar aleatoriamente un registro del archivo CSV
    registro_aleatorio = random.choice(datos_csv)
    lista.append(registro_aleatorio)
  return lista


def organizar_parqueadero(lista):
  parqueadero_organizado = []
  for estudiante in lista:
    nombre = estudiante["nombre"]
    id = estudiante["id"]
    perfil = estudiante["perfil"]
    prioridad = estudiante["Prioridad"]
    if isinstance(perfil, str) and perfil != "comun":
      prioridad = 1000 if perfil == 'honor' or perfil == 'ecologico' else 0
      parqueadero_organizado.append({
          "nombre": nombre,
          "id": id,
          "perfil": perfil,
          "Prioridad": prioridad
      })
  return sorted(parqueadero_organizado,
                key=lambda x: x["Prioridad"],
                reverse=True)


def mostrar_parqueadero(parqueadero):
  print(colors.MAGENTA + "Parqueadero:" + colors.RESET)
  nodo_actual = parqueadero.primero
  while nodo_actual:
    estudiante = nodo_actual.valor
    print(
        f"Nombre: {estudiante['nombre']}, ID: {estudiante['id']}, Perfil: {estudiante['perfil']}, prioridad: {estudiante['Prioridad']}"
    )
    nodo_actual = nodo_actual.siguiente


def main():
  '''#Descomentar en caso de mostrar todo el dataset
  parqueadero = obtener_lista_csv("dataset.csv")
  for vehiculo in parqueadero:
    nombre = vehiculo["nombre"]
    id = vehiculo["id"]
    perfil = vehiculo["perfil"]
    print(f"Nombre: {nombre}, ID: {id}, Perfil: {perfil}")
  '''

  dataset = "dataset.csv"  # Nombre del archivo CSV

  # Generar un tamaño aleatorio para la lista
  tamano_aleatorio = random.randint(1, 10)

  # Crear la cola enlazada para representar el parqueadero
  parqueadero = Cola()

  # Generar la lista de diccionarios aleatoria desde el archivo CSV
  lista_aleatoria_desde_csv = generar_lista_aleatoria_desde_csv(
      dataset, tamano_aleatorio)

  # Organizar la lista aleatoria por prioridad y encolar en la cola
  lista_organizada_desde_csv = organizar_parqueadero(lista_aleatoria_desde_csv)
  for estudiante in lista_organizada_desde_csv:
    parqueadero.encolar(estudiante)

  # Mostrar el parqueadero organizado por prioridad
  mostrar_parqueadero(parqueadero)


if __name__ == "__main__":
  main()
