import math
from random import randint


random_number = randint(100, 999)
print(f'The random number is: {random_number}')

result = 0

# Solution A
# O(n)
# for digit in str(random_number):
#    result = result = int(digit)

# Solution B
# O(n)
#  random_number = 321  Expected Result = 6
while random_number != 0: # 321
    result = result + (random_number % 10)
    random_number = random_number // 10

print(f'Result: {result}')
