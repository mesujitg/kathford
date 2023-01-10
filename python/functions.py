# function
'''
1. parameterized 2. non parameterized

1. return type 2. non return type
'''

def add(a, b):
    # print(a+b)
    return a+b


n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))
add(n1, n2)

# a = int(input('Enter first number'))
# b = int(input('Enter second number'))
# add(a, b)


def add_np():
    a = int(input('Enter first number'))
    b = int(input('Enter second number'))
    print(a+b)

# add_np()


def check_prime_number():
    n = input('Enter a number')
    # isdigit, isalpha, isalphanum, len
    if not n.isdigit():
        print('Invalid entry')
        check_prime_number()

    a = int(n)
    for i in range(2, a//2 + 1):
        if a%i == 0:
            print('Composite')
            break
    else:
        print('Prime')

    check_prime_number()



def check_prime_number1():
    try:
        a = int(input('Enter a number'))
        for i in range(2, a//2 + 1):
            if a%i == 0:
                print('Composite')
                break
        else:
            print('Prime')
    except Exception as e:
        print('Invalid entry: ', e)
    finally:
        check_prime_number1()


check_prime_number1()



def sub(a, b):
    print(a+b)

# positional arguements
sub(5, 6)   

# keyword arguements
sub(b=6, a=5)
