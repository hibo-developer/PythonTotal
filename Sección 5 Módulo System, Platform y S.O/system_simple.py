import sys
from datetime import datetime

# print('hola mundo')
# sys.stdout.write('hola mundo desde std out!\n')
# sys.stdout.flush()
# # Cursor/PowerShell no pinta stderr en rojo por sí solo: hay que usar ANSI
# sys.stderr.write('\033[91mhola tenemos un problema std error!\033[0m\n')

try:
    date_event = datetime.strptime('11-10-202', '%d-%m-%Y')
    print(date_event)
except ValueError as err:
    sys.stderr.write(f'Error con el formato de fecha {err}\n')  
    sys.exit(1)  

print('Otra tarea')
sys.exit(0)
