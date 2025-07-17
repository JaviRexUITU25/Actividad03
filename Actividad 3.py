#Fabritzio Lopez
#Javier Huertas
while True:
    print("---------Menú Principal---------")
    print("1. Conversión de unidades.")
    print("2. Conversión de temperatura.")
    print("3. Salir del programa.")
    option= int(input("-----Elija una de las opciones------: "))
    if option == 1:
        while True:
            print("---------Menú de conversiones---------")
            print("1. Conversión de metros a centimetros.\n")
            print("2. Conversión de centimetros a metros.\n")
            print("3. Conversión de kilogramos a libras.\n")
            print("4. Conversión de libras a kilogramos.\n ")
            print("5. Volver al menu principal.")
            opc= int((input("------Ingrese una opción de conversiones------: ")))
            if opc == 1:
                metros= int(input("Ingrese la cantidad de metros que quiere convertir a centimetros: "))
                cm= metros * 100
                print(f"La cantidad de {metros} metros equivale a {cm} centimetros.")
            elif opc == 2:
                centimetros= int(input("Ingrese la cantidad de centimetros que quiere convertir a metros: "))
                m= centimetros / 100
                print(f"La cantidad de {centimetros} centimetros equivale a {m} metros.")
            elif opc == 3:
                kilogramos= int(input("Ingrese la cantidad de kilometros que quiere convertir a libras: "))
                libras= kilogramos * 2.2046
                print(f"La cantidad de {kilogramos} kg equivale a {libras} lbs.")
            elif opc == 4:
                lb = int(input("Ingrese la cantidad de libras que quiere convertir a kilogramos: "))
                kg= lb / 2.2046
                print(f"La cantidad de {lb} lbs equivale a {kg} kgs.")
            elif opc == 5:
                break
            else:
                print("No existe esta opcion, intentalo de nuevo: ")
    #option= int(input("-----Elija una de las opciones------: "))
    if option == 2:
        while True:
            print("---------Conversion de temperatura---------")
            print(("1. Celcius a Fahrenheit\n"
                    "2. Fahrenheit a Celcius\n"
                    "3. Volver al menú principal."))
            opc = int((input("-----Ingrese la opción que desea-----: ")))
            if opc == 1:
                Cgrades = int(input("Ingrese la cantidad de grados Celcius: "))
                fah = 9/5 * Cgrades + 32
                print(f"La cantidad en grados fahrenheit es de: {fah} grados")
            elif opc == 2:
                fahrenheit = int(input("Ingrese la cantidad de grados Fahrenheit: "))
                cel = fahrenheit - 32 / 1.8
                print(f"La cantidad en grados Celcis es de: {cel} grados")
            elif opc == 3:
                break
            else:
                print("No existe esta opcion, intentalo de nuevo: ")
    #option= int(input("-----Elija una de las opciones------: "))
    if option == 3:
        while True:
                print("¡Gracias por usar el programa!")
                break
        break


