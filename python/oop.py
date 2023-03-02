'''
OOP
----
Class & Objects

Features of OOP
1. Encapsulation
2. Inheritance
3. Polymorphism
    a) Method overloading
    b) Method overriding
4. Abstraction (Interface)
'''

'''
Online News Portal
    User
        name, mobile, email, username, password
        register(), update(), view(), login(), delete()
    News
        topic, date, details, author, category  
        add() view() update() view()
    Comment
        fullname, email, comments, status(approved/requested)
        add() view() update() delete()
    

Online Student Enrollment
    User
        name, mobile, email, username, password, type
        register(), update(), view(), login(), delete()
    Course
        title duration fee shift affiliation department status
        add() view() update() delete() 
    Enrollment
        user course date

Online Job Portal
    User
        name, mobile, email, username, password, image, cv, type status
        register(), update(), view(), login(), delete()
    JobSeeker
    Employer
    Job
        title detail requirement salary company vacancy_no category, deadline, status
        add() update() view() delete()
    Application
        user job


Online Shopping (E-Commerce)
    User
        name, mobile, email, username, password, image, cv, type status
        register(), update(), view(), login(), delete()
    Customer
    Seller
    Product
        name price details stock features category brand types status
        add() view() update() delete()
    Order, Cart, Wishlist
        user product date

'''

class User:
    full_name = ''
    mobile = ''
    email = ''
    address = ''
    username = ''
    password = ''
    type = ''

    def setProperties(self):
        pass

    def register(self):
        pass

    def view(self):
        pass

    def login(self):
        pass

    def search(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


from abc import ABC, abstractmethod

# encapsulation
class Animal(ABC):

    # def __init__(self):
    #     self.__color = ''
    #     self.__height = ''
    #     self.__weight = ''

    def __init__(self, color_value, height_value, weight_value):
        self.__color = color_value
        self.__height = height_value
        self.__weight = weight_value

    # setters & getters
    def setColor(self, value):
        self.__color =  value

    def getColor(self):
        return self.__color

    @abstractmethod
    def move(self):
        pass
    

# animal = Animal('white', '2 ft', '10kg')
# animal.setColor('white')
# print(animal.getColor())

# inheritance

class Dog(Animal):
    def __init__(self, color_value, height_value, weight_value, food):
        self.food = food
        super().__init__(color_value, height_value, weight_value)
    
    def move(self):
        print('It Walks')

class Cat(Animal):
    def move():
        print('It walks')


class Crocodile(Animal):
    def move(self):
        print('It crawls')


class Bird(Animal):
    def move(self):
        print('It flies')


d = Dog('black', '1ft', '5 kg', 'abc')
d.move()

c = Crocodile('black', '1.5 ft', '35 kg')
c.move()

b = Bird('blue', '5 inch', '1 kg')
b.move()



# def add(a, b):
#     return a+b

def add(a, b, c=0):
    return a+b+c

print(add(5, 10))
print(add(5, 10, 15))


