import machine

# Definir códigos ANSI para colores
RESET = "\x1B[0m"
RED = "\x1B[31m"
GREEN = "\x1B[32m"
YELLOW = "\x1B[33m"
BLUE = "\x1B[34m"

# Imprimir texto en diferentes colores
print(RED + "Este texto es rojo" + RESET)
print(GREEN + "Este texto es verde" + RESET)
print(YELLOW + "Este texto es amarillo" + RESET)
print(BLUE + "Este texto es azul" + RESET)
# Imprimir texto normal
print("hola mundo...")
