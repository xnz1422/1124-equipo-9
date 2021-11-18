from src.utils import *

def main():
    opcion='0'
    while opcion!='8':
        print("1- Reemplazar espacios")
        print("2- Invertir mayúsculas/minúsculas")
        print("3- Reemplazar caracter")
        print("4- Capitalizar nombre y apellido")
        print("5- Obtener subcampeón")
        print("6- Triángulo")
        print("7- Contar letras")
        print("8- Salir")
        opcion=input("Ingrese una opcion: ")
        if opcion=='1':
            cadena=input("Ingrese una cadena de caracteres: ")
            print(reemplazar_espacios(cadena))
            input("Presione enter para volver al menú...")
        elif opcion=='2':
            cadena=input("Ingrese una cadena de caracteres: ")
            print(may_min(cadena))
            input("Presione enter para volver al menú...")
        elif opcion=='3':
            cadena=input("Ingrese una cadena de caracteres: ")
            indice=input("Ingrese el índice a reemplazar: ")
            caracter=input("Ingrese el caracter de reemplazo: ")
            print(reemplazar_caracter(cadena,indice,caracter))
            input("Presione enter para volver al menú...")
        elif opcion=='4':
            cadena=input("Ingrese nombre y apellido: ")
            print(capitalizar(cadena))
            input("Presione enter para volver al menú...")
        elif opcion=='5':
            lista=input("Ingrese una lista de números separados por espacio: ").split()
            print(subcampeon(lista))
            input("Presione enter para volver al menú...")
        elif opcion=='6':
            altura=input("Ingrese la altura del triángulo: ")
            triangulo(altura)
            input("Presione enter para volver al menú...")
        elif opcion=='7':
            cadena=input("Ingrese nombre empresa: ")
            mas_usados(cadena)
            input("Presione enter para volver al menú...")
        elif opcion=='8':
            print("Fin del programa")
        else:
            input("Opción inválida, presione enter para volver al menú...") 

if __name__ == "__main__":
    main()