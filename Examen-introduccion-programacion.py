"""
cajero
consultar saldo, retirar dinero, depositar dienro y salir

requiasitos
saldo = 1000
a. Consultar saldo
b. Depostiar dinero
c. Retirar dinero
d. Salir

Repetir menu hasta que le usuario seleccione salir o precione 0

funciones separadas cada opcion:
ConsultarSaldo()
Depositar()
Retirar()

validar:
El monto a depositar o retirar sea mayor que 0
Que no se pueda retirar mas dinero del disponible

Usar condicionales dentro de las funciones a retirar
Mosrar mensajes claros
"""

def ConsultarSaldo(saldo):
    print("1. Consultar Saldo.")
    print("Tu saldo actual es: $", saldo)

def Depositar(saldo):
    print("2. Depositar.")
    deposito = int(input("Cuanto dinero deseas depositar?: $"))
    if deposito > 0:
        saldo = saldo + deposito
        print("Tu saldo actual es: $", saldo)
    else:
        print("Monto invalido, intenta nuevamente.")
        input("Presiona ENTER para reintentar:")
        print("\n\n")
        deposito = int(input("Cuanto dinero deseas depositar?: $"))

        return saldo

def Retirar(saldo):
    print("3. Retirar")
    retiro = int(input("Cuanto dinero deseas retirar?: $"))
    if retiro <=0 or retiro > saldo:
        print("Monto invalido, o saldo insuficiente, su saldo actual es: $", saldo)
        return
    else:
        saldo = saldo - retiro
        print("Retiro existo, retiraste: $", retiro, ". Tu saldo actual es: $", saldo)

saldo = int(1000)

def menu():
    print("""
****MENU CAJERO****
1. Consultar Saldo
2. Depositar Dinero
3. Retirar dinero
4. Salir
-------------------
""")

def leerOpcion():
    opcion = input(">>> Opcion?: ")
    if opcion == "0":
        opcion = "4"
    while opcion < "1" or opcion > "4":
        print("Opcion invalida.")
        input("Presione ENTER para reintentar. ")
        print("\n\n")
        menu()
        opcion = input(">>> Opcion?: ")

    return int(opcion)

while True:
    menu()
    opcion = leerOpcion()
    match opcion:
        case 1:
            ConsultarSaldo(saldo)
        case 2:
            Depositar(saldo)
        case 3:
            Retirar(saldo)
        case 4:
            print("Gracias por usar nuestros servicios. :D")
            break

input("Presiona ENTER para continuar.")



