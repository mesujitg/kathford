'''
Collections in Python
1. Tuple: immutable, indexed, ordered, allows duplicate member
2. List: mutuable, indexed, ordered, allows duplicate member
3. Set: element can not be changed but new elements can be added,
        unindexed, unordered, doesnot allow duplicate member
4. Dictionary: mutuable, indexed, ordered, no duplicate keys

(Range)

user_info = ['ram', 40, 100000.0, True]

students_list = ['ram', 'shyam', 'hari', 'sita', 'gita', 'shyam']
students_tuple = ('ram', 'shyam', 'hari', 'sita', 'gita', 'shyam')
students_set = {'ram', 'shyam', 'hari', 'sita', 'gita', 'shyam'}
students_dict = {12001: 'ram', 12002: 'shyam', 12003:'hari', 
                12004: 'sita', 12005: 'gita', 12006: 'shyam'}
user_info_dict = {'name': 'ram kumar', 'age': 40, 'salary': 100000.0,
                    'is_married': True}

for i in students_dict:
    print(i, ': ', students_dict[i])
'''

# print(students_list)
# print(students_tuple)
# print(students_set)
# print(user_info_dict)
# user_info_dict['age'] = 41
# user_info_dict['address'] = 'Kathmandu'
# print(user_info_dict)


# multidimensional collection
'''
a = [[], [], []]
b = [(), (), ()]
c = [{}, {}, {}]
d = ((), (), ())
e = ([], [], [])
f = ({}, {}, {})
g = {'key1': {}, 'key2': {}, 'key3': {}}
h = {'key1': [], 'key2': [], 'key3': []}
i = {'key1': (), 'key2': (), 'key3': ()}

students = [
    ['ram', 'kathmandu', 'ram@email.com', '9841112233'],
    ['ram', 'kathmandu', 'ram@email.com', '9841112233'],
    ['ram', 'kathmandu', 'ram@email.com', '9841112233'],
]

students = [
    {'name':'ram', 'address': 'kathmandu', 'email':'ram@email.com', 'mobile':'9841112233'},
    {'name':'shyam', 'address': 'lalitpur', 'email':'ram@email.com', 'mobile':'9841112233'},
    {'name':'hari', 'address': 'bhaktapur', 'email':'ram@email.com', 'mobile':'9841112233'}
]


students = {
    'name': ['ram', 'shyam', 'hari'],
    'address': [],
    'email': [],
    'mobile': []
}
'''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
        'Thursday', 'Friday', 'Saturday']
'''
n = int(input('Enter a number'))

if n <= 0 or n > 7:
    print('invalid')
else:
    print(days[n-1])
'''
n = input('Press Enter to see next')



