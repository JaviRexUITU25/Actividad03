#Fabritzio Lopez
#Javier Huertas
while True:
    print("Menú Principal")
    print("1. Conversión de unidades.")
    print("2. Conversión de temperatura.")
    print("3. Salir del programa.")
    opcion= int(input("Elija una de las opciones:"))
    if opcion == 1:
        while True:
            print("Mené de conversiones")
            print("1. Conversión de metros a centimetros.")
            print("2. Conversión de centimetros a metros.")
            print("3. Conversión de kilogramos a libras.")
            print("4. Conversión de libras a kilogramos. ")
            opc= int(input("Ingrese una opción de conversiones: "))
            if opc == 1:
                metros= int(input("Ingrese la cantidad de metros que quiere convertir a centimetros: "))
                cm= metros * 100
                print(f"La cantidad de {metros} metros equivale a {cm} centimetros.")
            elif opc == 2:
                centimetros= int(input("Ingrese la cantidad de centimetros que quiere convertir a metros: "))
                m= centimetros / 100
                print(f"La cantidad de {centimetros} centimetros equivale a {m} metros.")
