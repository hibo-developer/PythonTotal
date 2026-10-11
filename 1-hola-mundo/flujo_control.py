# for num in range(10):
#     if num  == 5:
#         break
#     print("El numero es: ", num)
  
# print("Fin del programa")

# for num in range(10):
#     if num  == 5:
#         pass
#     print("El numero es: ", num)

# print("Fin del programa")

# for num in range(10):
#     if num  == 5:
#         continue
#     print("El numero es: ", num)

# print("Fin del programa")

user = ['admin', 'user', 'anonymous']
intentos = 0
for user in user:
    if user == 'anonymous':
        intentos += 1
        print("Usuario no autorizado")
        continue
    print("Bienvenido usuario: ",user, ", número de intentos: ", intentos)
print("Fin del programa")