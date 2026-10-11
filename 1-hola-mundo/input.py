def main():
    name = input('Introduce el nombre del producto: ')
    # print(f'Producto - {name}')

    precio = float(input('Introduce el precio del producto: '))
    # print(f'El precio es - {precio}€')


    peso = float(input('Introduce el peso en gramos: '))
    # print(f'Pesa - {peso}grs.')
    print(f'Producto: {name} \nPrecio: {precio}€\nPeso: {peso}grs')
try:
    main()   
except ValueError:
    print('Debe introducir bien los datos, decimales con punto.')
    main()