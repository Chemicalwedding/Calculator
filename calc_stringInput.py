import math
#import re

compute = ['+', '-', '*']
calc = input()

#calculator COMPUTE
index = calc.index('+')
value  = float(calc[0:index])
value2 = float(calc[index:])
list_of_floats = [value, value2]

#strategy pattern
if calc[index:-1] == '+':
  power = math.fsum(list_of_floats)
if calc[index:-1] == '-':
	power = (value - value2)
if calc[index:-1] == '*':
	power = (value * value2)
	
print(index)
print(power)
print(compute[1])