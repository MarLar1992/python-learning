"""def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
#greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")
print("Finish")

"""
import self as self

"""
def square(number):
    print(number * number)


print(square(3))
"""

"""
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
    """
"""
age = 36
txt = "My name is John, I am {} "
print(txt.format(age))
 """

"""
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)

            x = Person("John", "Doe")
            x.printname()
"""

"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""

"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
"""

"""
def greeting(name):
    print("Hello" + name)
    import app5
    app5.greeting("Jonathan")
    """

"""
import datetime

x = datetime.datetime.now()
print(x)
"""

"""
#change python to json
import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)
print(y)
"""

"""
#change json to python
import json

x = '{"name": "John", "age": 30, "city": "New York"}'
y = json.loads(x)
print(y["age"])
"""

"""
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
"""

"""
import json
Convert a Python object containing all the legal data types:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
    ]
}

y = json.dumps(x)
print(y)
"""

"""
try:
    print(x)
except:
    print("An exception occured")
"""

"""
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
"""

"""
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
    """

"""
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
"""

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))