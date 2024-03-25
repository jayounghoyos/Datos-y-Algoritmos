# Colores ANSI
class colors: #Creo la clase colors
    RESET = '\033[0m' #Este es el color base de la terminal
    BOLD = '\033[1m'#Creo el color con su respectivo ANSI
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

class Pila: #Se crea la clase pila
    def __init__(self): # Se crea el constructor con una lista vacía
        self.items = []

    def apilar(self, elemento): #Método de apilamiento
        self.items.append(elemento)

    def desapilar(self): #Eliminación del último elemento por ser una pila LIFO
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):# Verificación ¿vació o no?
        return len(self.items) == 0

    def imprimir(self):#Imprime la pila
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
            Self_primero = nuevo_nodo

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
    def __init__(self, nombre, id, categoria):
        self.nombre = nombre
        self.id = id
        self.categoria = categoria

    def recargar_creditos(self, num_creditos):
        self.creditos = num_creditos


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyC')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
