# i = 0

# while i <= 5:
#     print(f'Contador es {i}')
#     i += 1

# print('Fin del programa')
# names = ['Juan', 'Pedro', 'Maria', 'Jose', 'Ana']
# contador = 0
# # print(len('Robert'))
# while contador < len(names):
#     print(f'Nombre en posición {contador} es {names[contador]}')
#     contador += 1

# print('Fin del programa')

# i = 1
# while True:
#     print(f'Contador es {i}')
#     i += 1
#     if i > 5:
#         break

# print('Fin del programa')

import random

secreto = random.randint(1, 10)

while True:
    number = int(input('Ingrese un numero: '))
    if number == secreto:
        print('Adivinaste el numero')
        break
    elif number < secreto and number > 0 and number < 11:
        print('El numero es mayor')
    elif number > secreto and number > 0 and number < 11:
        print('El numero es menor')
    else:
        print('El numero no es válido, ingrese un numero entre 1 y 10')
        continue

print(f'Fin del programa, el número secreto era {secreto}')









