#variables
x = 10
y = "Hello"

#unlike other programming languages in python you don't need to assign a variable type during the declaration, it is created by default
#when you assign a value to it

a, b = 10, "test"
print(a,b)
#this way you can declare multiple variables at once

a = b = 10
#and declare many variables with the same value

print(x)
print(y)

print(x); print(y)

#this two pieces of code will create the same output, you can use semicolons to separate two statements but these are rarely used
#Best practice: Put each statement on its own line so your code is easy to understand.

print(x, y)
print(10, "hello world")
x = str(x)
print(x + y)
x = int(x)

#with , you can concat different variables, even with different types and it will automatically generate a space between them
#with + you can do the same but only with str variables, and it won't have any separation between them, it has to be given expressly
print("Hello World!", end=" ")
print("I will print on the same line.")

#in python you can cast any variable into another one even if those variable types are not related at all
print(x)
x = "hello, now x is a str"
print(x)
x = 10
print(x, " back to normal")

fruits = ["banana", "apple", "cherry"]
x, y, z = fruits
print(x,y,z)
#this is called "unpacking" you can acces the content of a list, array or tuple with simple variables

#string
#in python string variables are arrays, so the inherit some of the array caracteristics
txt = "Hello world"
print(len(txt))
print(txt[0])

for x in txt:
    print(x)

print("world" in txt)

if "world" in txt:
    print("true")

print(txt[2:5]) #print the characters from the positions 2 to 5
print(txt[:5]) #print the characters from the beggining to the position 5
print(txt[2:]) #print the character from the position 2 to the end

age = 20
txt2 = f"My name is Axel, I am {age}"
print(txt2)
