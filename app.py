
from function import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

def main():
    # Bucle principal del programa
    salir = True
    while salir:
        mostrar_menu()
        print()
        try:
            option = int(input('Elige una opción: '))
        except:
            print(f'{Back.RED} Introduce una opción correcta')

        if option == 1:
            moverte_directorio_especifico()
        elif option == 2:
            subir_un_nivel()
        elif option == 3:
            entrar_en_directorio_de_directorio_actual()
        elif option == 4:
            listar_contenido()
        elif option == 5:
            crear_directorio()
        elif option == 6:
            crear_archivo()
        elif option == 7:
            escribir_en_archivo()
        elif option == 8:
            eliminar_elemento()
        elif option == 9:
            mostrar_informacion()
        elif option == 0:
            salir = False
        else:
            print(f'{Back.RED} Introduce una opción correcta')



if __name__ == '__main__':
    main()