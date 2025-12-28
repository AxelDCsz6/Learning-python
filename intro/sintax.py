#variables
x = 10
y = "Hello"

#unlike other programming languages in python you don't need to assign a variable type during the declaration, it is created by default
#when you assign a value to it

print(x)
print(y)

print(x); print(y)

#this two pieces of code will create the same output, you can use semicolons to separate two statements but these are rarely used
#Best practice: Put each statement on its own line so your code is easy to understand.

print(x, y)
print(10, "hello world")

#concat different variables, even with different types

print("Hello World!", end=" ")
print("I will print on the same line.")

#in python you can cast any variable into another one even if those variable types are not related at all
print(x)
x = "hello, now x is a str"
print(x)
x = 10
print(x, " back to normal")


