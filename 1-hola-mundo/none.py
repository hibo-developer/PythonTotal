
texto = input('Ingrese un texto: ').strip()
if texto:
    print(f'El texto no está vacío: {texto}')
else:
    print('El texto está vacío.')


personas = ['Juan', 'María', 'Pedro']
if personas:
    print(f'La lista de personas no está vacía: {personas}')
if personas is not None:
    print(f'La lista de personas no está vacía: {personas}')

