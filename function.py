import os
import shutil
from datetime import datetime
import stat
from colorama import Fore, Back, Style, init

init(autoreset=True)

def mostrar_menu():
    # Muestra las opciones disponibles
    menu = '''MENÚ PRINCIPAL
1. Moverte a un directorio específico
2. Subir un nivel en arbol de direcctorios
3. Entrar a un directorio del directorio actual
4. Listar contenido del directorio actual
5. Crear un nuevo directorio
6. Crear un archivo de texto
7. Escribir texto en un archivo existente
8. Eliminar un archivo o directorio
9. Mostrar información del archivo
0. Salir'''
    print()
    print(Fore.BLUE + Style.BRIGHT + menu)

def moverte_directorio_especifico():
    try:
        path = input("¿Cual es la ruta del directorio al que quieres ir?\n")
        os.chdir(path)
        print(Back.GREEN + f"Estás en la ruta {path}")
        print("SU CONTENIDO ES:")
        listar_contenido()
    except:
        print(Back.RED + "La ruta expecificada no es una ruta válida")

def subir_un_nivel():
    os.chdir("..")

def entrar_en_directorio_de_directorio_actual():
    try:
        directorio = input("¿Cual es el directorio al que quieres ir?\n")
        os.chdir(directorio)
        print(Back.GREEN + f"Estás en la directorio {directorio}")
        print("SU CONTENIDO ES:")
        listar_contenido()
    except:
        print(Back.RED + "El directorio expecificado no es una directorio válido")

def listar_contenido():
    # Lista archivos y carpetas del directorio actual
    directorio_actual = os.getcwd()
    for i in os.listdir(directorio_actual):
        if os.path.isfile(i):
            print(Fore.BLUE + 'Archivo' + Fore.GREEN +  ' -> ' + Fore.CYAN + i)
        else:
            print(Fore.BLUE + 'Fichero' + Fore.GREEN +  ' -> ' + Fore.MAGENTA + i)

def crear_directorio():
    # Crea una nueva carpeta
    dic_name = input("¿Que nombre le quires poner a tu directorio?\n")
    os.mkdir(dic_name)
    print(Back.GREEN + f'El directorio {dic_name} se ha creado con éxito en la ruta {os.getcwd()}\{dic_name}')

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    arch_name = input("¿Que tipo de archivo quieres crear?\n")
    open(f'{arch_name}.txt', 'w')
    print(Back.GREEN + f'El archivo {arch_name}.txt se ha creado con éxito en la ruta {os.getcwd()}\{arch_name}.txt')

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    arch_name = input("¿En qué archivo quieres escribir?\n")
    lista_directorios = os.listdir(os.getcwd())
    if arch_name in lista_directorios:
        with open(arch_name, 'a', encoding='utf-8') as file:
            texto= input("¿Qué quieres escribir en el archivo?\n")
            file.writelines(texto)
            print(Fore.GREEN + f'El archivo {arch_name} ha sido actualizado correctamente')
    else:
        print(Fore.RED + f'El archivo {arch_name} no está dentro de los archivos de este directorio.')


def eliminar_elemento():
   # Elimina un archivo o carpeta
    arch_dicect = input("¿Qué archivo o directorio quieres eliminar?\n")
    lista_directorios = os.listdir(os.getcwd())

    def force_remove(func, path, _):
        """
        Si un archivo o carpeta no puede eliminarse por permisos (solo lectura, etc.),
        cambia sus permisos y reintenta.
        """
        os.chmod(path, stat.S_IWRITE)
        func(path)

    if arch_dicect in lista_directorios:
        if os.path.isfile(arch_dicect):
            os.remove(arch_dicect)
            print(Fore.GREEN + f'El archivo "{arch_dicect}" ha sido eliminado correctamente.')
        elif os.path.isdir(arch_dicect):
            try:
                shutil.rmtree(arch_dicect, onerror=force_remove)
                print(Fore.GREEN + f'El directorio "{arch_dicect}" y su contenido han sido eliminados correctamente.')
            except PermissionError:
                print(Fore.RED + f'No tienes permisos para eliminar "{arch_dicect}". Ejecuta el programa como administrador.')
            except Exception as e:
                print(Fore.RED + f'Error al eliminar el directorio: {e}')
        else:
            print(Back.RED + f'"{arch_dicect}" no es ni un archivo ni un directorio reconocido.')
    else:
        print(Back.RED + f'El archivo o directorio "{arch_dicect}" no está dentro del directorio actual.')


def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    directorio_actual = os.getcwd()
    for i in os.listdir(directorio_actual):
        if os.path.isfile(i):
            print(f'{Fore.BLUE} Archivo {Fore.GREEN} -> {Fore.CYAN} {i:<20} Tamaño: {str(os.path.getsize(i)):<10} Fecha Ulima Modificación: ' + datetime.fromtimestamp(os.path.getmtime(i)).strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print(f'{Fore.BLUE} Fichero {Fore.GREEN} -> {Fore.CYAN} {i:<20} Tamaño: {str(os.path.getsize(i)):<10} Fecha Ulima Modificación: ' + datetime.fromtimestamp(os.path.getmtime(i)).strftime('%Y-%m-%d %H:%M:%S'))