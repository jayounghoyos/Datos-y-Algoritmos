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
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(colors.RED + f' Hi, {name}' + colors.RESET)  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
