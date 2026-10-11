def main():
    name = input('Cómo te llamas? \n')
    age = int(input('Qué edad tienes? \n'))
    print(f'Hola {name}, tienes {age} años.')

try:
    main()
except ValueError:
    print('Error: debe introducir un número enteror para la edad!')
    main()