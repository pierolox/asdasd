print("¿la puerta esta abierta?")

var = int(input("ingrese 1 si la puerta esta abierta o 0 si la puerta esta cerrada: "))

while True:
    try:
        if var == 1 or var == 0:
            print("la puerta esta abierta" if var == 1 else "la puerta esta cerrada")
        else:
            print("solo se puede ingresar el numero 0 y 1")

        var = int(input("ingrese 1 si la puerta esta abierta o 0 si la puerta esta cerrada: "))
        
    except ValueError:
        print("debe ingresar numeros")