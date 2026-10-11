# numero = int(input("Ingrese un numero del 1 al 3: "))

# match numero:
#     case 1:
#         print("El numero es 1")
#     case 2:
#         print("El numero es 2")
#     case 3:
#         print("El numero es 3")
#     case _:
#         print("El numero no es 1, 2 o 3")
# print("Fin del programa")     


# def option(numero):
#     response = None
#     match numero:
#         case 1:
#             response = f"El numero es {numero}"
#         case 2:
#             response = f"El numero es {numero}"
#         case 3:
#             response = f"El numero es {numero}"
#         case _:
#             response = "El numero no es 1, 2 o 3"
#     return response
# result = option(int(input("Ingrese un numero del 1 al 3: ")))
# print(result)
# print("Fin del programa")




def option(name):
    respuesta = None
    match name:
        case 'Pepe':
            respuesta = 'Hola Pepe'
        case 'Juan':
            respuesta ='Hola Juan'
        case 'María':
            respuesta ='Hola María'
        case _:
            respuesta ='Hola invitado...'
    return respuesta

resultado = option(str(input('Introduce el nombre de la persona: ')))
print(resultado)



