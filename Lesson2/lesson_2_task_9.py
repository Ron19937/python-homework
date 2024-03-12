var_1 = 37
var_2 = 99

a = input('var_1: ')
b = input('var_2: ')
 
buf = var_1
var_1 = var_2
var_2 = buf
 
print('var_1 =', var_1)
print('var_2 =', var_2)