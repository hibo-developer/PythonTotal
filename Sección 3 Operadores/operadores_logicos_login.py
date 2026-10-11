# usuarios = {
#     "Andrés": "1234",
#     "Juan": "5678",
#     "María": "abcd",
#     "Pedro": "efgh"
# }

# usuario_input = input("Ingrese su nombre de usuario: ")

# if usuario_input in usuarios:
#     contraseña_input = input("Ingrese su contraseña: ")
#     if contraseña_input == usuarios[usuario_input]:
#         print("¡Inicio de sesión exitoso!")
#     else:
#         print("Contraseña incorrecta.")
# else:
#     print("Usuario no encontrado.")

# usuarios = {
#     "Andrés": "1234",
#     "Juan": "5678",
#     "María": "abcd",
#     "Pedro": "efgh"
# }

# intentos = 0

# while intentos < 3:
#     usuario = input("Ingrese su nombre de usuario: ")

#     if usuario in usuarios:
#         contraseña = input("Ingrese su contraseña: ")

#         if contraseña == usuarios[usuario]:
#             print("¡Inicio de sesión exitoso!")
#             break
#         else:
#             print("Contraseña incorrecta.")
#     else:
#         print("Usuario no encontrado.")

#     intentos += 1

# if intentos == 3:
#     print("Has excedido el número de intentos.")

usuarios = {
    "Andrés": "1234",
    "Juan": "5678",
    "María": "abcd",
    "Pedro": "efgh"
}

def validar_usuario(usuario):
    if usuario.strip() == "":
        return False
    if len(usuario) < 3:
        return False
    return True

def validar_contraseña(contraseña):
    if contraseña.strip() == "":
        return False
    if len(contraseña) < 4:
        return False
    return True

def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    while not validar_usuario(usuario):
        print("El usuario no es válido. Debe tener al menos 3 caracteres.")
        usuario = input("Ingrese un nombre de usuario: ")

    contraseña = input("Ingrese una contraseña: ")
    while not validar_contraseña(contraseña):
        print("La contraseña no es válida. Debe tener al menos 4 caracteres.")
        contraseña = input("Ingrese una contraseña: ")

    usuarios[usuario] = contraseña
    print(f"Usuario '{usuario}' registrado correctamente.")

def iniciar_sesion():
    intentos = 0

    while intentos < 3:
        usuario = input("Ingrese su nombre de usuario: ")
        if not validar_usuario(usuario):
            print("Nombre de usuario inválido.")
            intentos += 1
            continue

        contraseña = input("Ingrese su contraseña: ")
        if not validar_contraseña(contraseña):
            print("Contraseña inválida.")
            intentos += 1
            continue

        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("¡Inicio de sesión exitoso!")
            return

        print("Usuario o contraseña incorrectos.")
        intentos += 1

    print("Has excedido el número máximo de intentos.")

while True:
    print("\n===== MENÚ DE LOGIN =====")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")