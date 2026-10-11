import random
import math
#
color = ['blue',
         'red',
         'green',
         'yellow',
         'purple',
         'orange',
         'pink',
         'black',
         'white',
         'gray']
#
# color_value = random.random()
# color_value *= len(color)
# color_value = math.floor(color_value)
# print('Color aleatorio:', color[color_value])
#
# print(len(color))

random_int = random.randint(1,len(color)-1)
print(random_int)

random_range = random.randrange(1,(5+1))
print(random_range)