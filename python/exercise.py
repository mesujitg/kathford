questions = ['What is area of Nepal?', 
        'What is the height of mount everest?', 
        'Who is first prime minister of nepal?', 
        'Pupulation of Nepal is:', 
        'First Nepali Movie is:']

options = [
    ('147181 sq km', '181147 sq km', '174818 sq km', '247181 sq km'),
    ('7747 m', '7848 m', '8848 m', '4484 m'),
    ('BP Koirala', 'Bhimsen Thapa', 'Kalu Pandey', 'Manmohan Adhikari'),
    ('39178900', '29178900', '49178900', '19178900'),
    ('Deuta', 'Xyz', 'Abc', 'Aama'),
]

answers = ['a', 'c', 'b', 'b', 'd']

# answers = ['147181 sq km', '8848 m', 'Bhimsen Thapa', '29178900', 'Aama']
score = 0

def show(n):
    print(questions[n])
    print('a. ', options[n][0])
    print('b. ', options[n][1])
    print('c. ', options[n][2])
    print('d. ', options[n][3])
    choice = input('Enter a/b/c/d: ')
    global score
    
    # if choice != 'a' or choice != 'b' or choice != 'c' or choice != 'd':
    while choice not in ['a', 'b', 'c', 'd']:
        print('Invalid Selection') 
        choice = input('Enter a/b/c/d: ')

    if choice == answers[n]:
        score += 1


for i in range(len(questions)):
    show(i)

print('Your Score is: ', score)


