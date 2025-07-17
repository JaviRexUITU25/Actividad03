#Fabritzio Lopez
#Javier Huertas
while True:
    print("-----Menú Principal-----")
    print("1. Conversión de unidades.")
    print("2. Conversión de temperatura.")
    print("3. Salir del programa.")
    opcion= int(input("Elija una de las opciones:"))
    print("-----------------------------------")
    if opcion == 1:
        while True:
            print("-----Menú de conversiones-----")
            print("1. Conversión de metros a centimetros.")
            print("2. Conversión de centimetros a metros.")
            print("3. Conversión de kilogramos a libras.")
            print("4. Conversión de libras a kilogramos. ")
            print("5. Volver al menu principal.")
            print("-----------------------------------")
            opc= int(input("Ingrese una opción de conversiones: "))
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
                print(f"La cantidad de {kilogramos} kg equivale a {libras:.2f} lbs.")
            elif opc == 4:
                lb = int(input("Ingrese la cantidad de libras que quiere convertir a kilogramos: "))
                kg= lb / 2.2046
                print(f"La cantidad de {lb} lbs equivale a {kg:.2f} kgs.")
            elif opc == 5:
                break
            else:
                print("Ingrese una opción del menú.")
