# print('Welcome')

'''
# variables & datatypes

name = 'ram kumar'
age = 40
salary = 100000.0
is_married = True

print('Name: ' + name)
print('Age: ', age)
print(f'Salary: { salary }')
print('Marital Status: ', is_married)


name = input('Enter your name: ')
salary = input('Enter your salary (per year): ')

print('Mr/Mrs ', name, ' your total tds amount on your annual income is:', float(salary)*0.15)

'''

'''
# operators
1. Arithmatic: + - * / ** // %
2. Logical: and or not
3. Relational: < > <= >= ==
4. Assignment: = += -= *= /= **= //= %=
5. Concatenation: +     ,
6. Membership: in       not in
7. Identity: is         is not

a = 10
b = 25
c = 10
# print(a>b or a==c)
# print(a != b)
# print(a != c)
a %= 4
# a //= 4
print(a)
'''

'''
Conditional statements
1. if 
2. if...else
3. if...elif...else


a = input('Enter first number')
b = input('Enter second number')

if a>b:
    print('First number is greater')
elif b>a:
    print('Second number is greater')
else:
    print('Equal')

print('Bye')
'''

# print if a user given number is odd or even
# a = int(input('Enter a number: '))
# if a%2 == 0:
#     print('Even')
# else:
#     print('Odd')

'''
Loops in Python
1. for
2. while
'''

# for(initialize; final_condition, increment/decrement)
# for(a=1; a<=10; a++)
'''
for i in range(10, 0, -2):
    print(i)


j=1
while j<=10:
    print(j)
    j += 1
'''

#print if a given number is prime or composite
'''
a = int(input('Enter a number'))
for i in range(2, a//2 + 1):
    if a%i == 0:
        print('Composite')
        break
else:
    print('Prime')
'''

# print day according to user given number. 
# 3 => Tuesday

# 9813903653 - Amrit

# print factorial of a user given number.
# print factors of a user given number.

# fibonacci's series less than 100
# 0 1 1 2 3 5 8 .......

# a = 0
# b = 1

# print(a)
# print(b)

# while a+b <= 100:
#     c = a+b
#     print(c)
#     a = b
#     b = c
        

'''
for i in range(100):
    c = a+b
    if c<=100:
        print(c)
        a = b
        b = c
    else:
        break
'''


# nested loop
# multiplication of a number
'''
n1 = 10
n2 = 10

for i in range(1, n1+1):
    for j in range(1, n2+1):
        print(i, 'x', j, '=', i*j, end=' ')
    print()
'''

'''
*           1       1           55555       12345       54321
**          22      12          4444        1234        4321
***         333     123         333         123         321
****        4444    1234        22          12          21
*****       55555   12345       1           1           1
'''

for i in range(5):
    for j in range(i+1):
        print(j+1, end=' ')
    print()

