from Tools.scripts.combinerefs import read

# Task 1: Welcome to Python
print('Task 1: Welcome to Python')
def print_hi(name, surname):
    print(f'Hello {name} {surname}! You just delved into Python. Great start!')

name = input("Write Name: ")
surname = input("Write Surname: ")

print_hi(name, surname)
input('Press "Enter" to next task!')

# Task 2: Python
print('Task 2: Python Art')

thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
input('Press "Enter" to next task!')

# Task 3: Title
print('Task 3: Title')
print('Title string: ', input('Write a string: ').title())
input('Press "Enter" to next task!')

# Task 4: Money
print('Task 4: Money')
amount = float(input('Amount of money: '))
round(amount, 2)
print('{0:,}'.format(amount))
input('Press "Enter" to next task!')

# Task 5: Carpet Design
height = int(input('Write a height of carpet: '))
width = height * 3

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('WELCOME'.center(width, '-'))

for stick_count in range(height-2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))
input('Press "Enter" to next task!')

# Task 6: Number multiply
print('Task 6: Number multiply')
result = 1
number = input('Write number: ')
number = int(number)
while number > 0:
    if number % 10 != 0:
        result = result * (number % 10)
    number = int(number / 10)

print(result)