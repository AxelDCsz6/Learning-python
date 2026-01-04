import sys

TRUTHY = {"true","t","1","yes","y"}
FALSY = {"false","f","0","no","n"}

#functions definition
def fib(n):
    """Todo lo puesto aqui sera tomado para python como un string de documentacion de la propia funcion"""
    a,b = 0,1
    while a < n:
        print(a, end=", ")
        a, b = b, a+b
    print()

#if statement and try-except
try:
    if len(sys.argv)<2:
        sys.exit(1)

    flag = sys.argv[1].strip().casefold()

    if flag in TRUTHY: 
        print("This is a true statement")
    elif flag in FALSY: 
        print("This is a false statement")
    else:
        print("valor no valido")

    if len(sys.argv) > 2:
        fib(int(sys.argv[2]))
except SystemExit:
    print("No argumentos entregados")

#for statements
print("Valores verdaderos:")
for x in TRUTHY:
    print(x, end=", ")

for x in range(10):
    print(x, end=", ")

print()
users = {'Hans': 'active', 'Éléonore': 'inactive', 'Jose': 'active'}

for user, status in users.items():
    if status == 'active':
        print(user)

step, start, end = 2, -10, 10

print(list(range(start, end, step)))

for x in enumerate(users):
    print(x)

for user, status in users.items():
    if status == 'active':
       continue 
    print(user)

#match statement
numero = 1
match numero:
    case 0:
        print("esta linea no se ejecutara")
    case 1:
        print("esta linea si se ejecutara")
    case 2:
        print("esta linea no se ejecutara")
    case 3:
        print("esta linea no se ejecutara")


