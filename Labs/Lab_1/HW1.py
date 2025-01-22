#HOME
print("Hello, World!")

#SYNTAX
if 5 > 2:
  print("Five is greater than two!")
if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

#COMMENTS
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#VARIABLES
x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)

x = str(3)
y = int(3)
z = float(3)

x = 5
y = "John"
print(type(x))
print(type(y))

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#DATA TYPES
x = 5
print(type(x))

#NUMBERS
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 2.8
z = 1j
a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#CASTING
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

#STRING
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello, World!"
print(a.upper())

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt1 = "We are the so-called \"Vikings\" from the north."
print(txt1)