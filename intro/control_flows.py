import sys

TRUTHY = {"true","t","1","yes","y"}
FALSY = {"false","f","0","no","n"}

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
except SystemExit:
    print("No argumentos entregados")


