import sys

if len(sys.argv) == 1:
    print("ningun argumento fue brindado")
else:
    print(f"argumentos: {sys.argv}")

print("Recorrido por todos los valores del arreglo")
for x in sys.argv:
    print(x)
