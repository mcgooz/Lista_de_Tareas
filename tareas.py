# Librerías: Avisos contiene todos los mensajes de aviso.
# datetime para mostrar la fecha. tabulate para mostrar la lista de tareas en una tabla.
# json para guardar y recuperar datos en un archivo json. random para mostrar varios mensajes de ánimo, despedida.
# time para dar un momento para leer los avisos.

from avisos import Avisos
from datetime import date
from tabulate import tabulate
import json
import random
import time


# Definir clase de tareas
class Lista_de_tareas:
    # Definir colores con códigos de ANSI.
    VERDE = "\033[92m"
    AZUL = "\033[94m"
    DEF_COLOR = "\033[0m"  # Resetear color

    def __init__(self, archivo):
        self.archivo = archivo  # Nombre del archivo o directorio del json
        self.tareas = self.check_json()  # Recuperar tareas del json, si existe.

    # Abrir y leer el json si existe. Si no, devolver una lista vacía.
    def check_json(self):
        try:
            with open(self.archivo, "r") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []

    # Representar objetos como strings
    def __str__(self):
        # Comprobar si hay entradas en la lista
        if self.tareas:
            listado = ""  # Inicializar una lista vacía.
            indice = 1  # Inicializar indice a 1
            # Iterar sobre las entradas para ver estado y asignar un string correspondiente.
            for tarea in self.tareas:
                if tarea["completada"]:
                    estado = "Completada"
                else:
                    estado = "Pendiente"
                # Construir string de tareas encontradas y agregar a la lista inicializada.
                listado += f"{indice}. {tarea['tarea']} - {estado}\n"
                # Actualizar número de indice.
                indice += 1
            # Devolver lista completa
            return listado
        # Si no hay entradas, devolver un mensaje de aviso.
        else:
            return "ninguna_tarea", None

    # Abrir el json y guardar la lista de tareas.
    def guardar(self):
        with open(self.archivo, "w") as archivo:
            json.dump(self.tareas, archivo, indent=4)

    # Método para agregar una tarea.
    def agregar(self, tarea):
        # Chequear si una tarea ya existe.
        for tarea_existente in self.tareas:
            if tarea_existente["tarea"] == tarea:
                return "tarea_ya_existe", tarea

        # Utilizar un diccionario para agregar una tarea a la lista y hacer seguimiento de su estado.
        self.tareas.append(
            {"tarea": tarea, "completada": False}
        )  # Por defecto, el estado será False.
        # Guardar la tarea en json.
        self.guardar()
        # Devolver mensaje de éxito
        return "tarea_agregada", tarea

    # Método para marcar como completada
    def completar(self, indice_tarea):
        # Usar try/except para pillar error de input
        try:
            # Buscar entrada en la lista y cambiar estado a True.
            indice_tarea = int(indice_tarea) - 1  # Menos uno por el indice cero.
            tarea = self.tareas[indice_tarea]
            if tarea["completada"]:
                return "tarea_ya_completada", tarea["tarea"]
            else:
                tarea["completada"] = True
                # Actualizar json
                self.guardar()
                # Devolver mensaje de éxito.
                return "tarea_completada", tarea["tarea"]

        # Si lo introducido no es válido, devolver mensaje de error.
        except IndexError:
            return "tarea_no_encontrada", None
        except ValueError:
            return "numero_invalido", None

    # Método para mostrar el listado
    def listar(self):
        tabla = ""
        if self.tareas:
            # Especificar cabeceras de las columnas de la tabla (tabulate)
            cabeceras = ["#", "Tarea", "Estado"]
            tabla = []
            # Inicializar variable para numerar entradas
            número = 1
            # Iterar sobre la lista
            for tarea in self.tareas:
                # Si completada es falso, poner pendiente con color correspondiente.
                if tarea["completada"] == False:
                    estado = self.AZUL + "Pendiente" + self.DEF_COLOR
                # Si completada es verdad, poner completada con color correspondiente.
                elif tarea["completada"] == True:
                    estado = self.VERDE + "Completada" + self.DEF_COLOR
                # Añadir fila a la tabla
                tabla.append([número, tarea["tarea"], estado])
                # Aumentar numero para la siguiente entrada
                número += 1
            # Generar tabla formateada.
            tabla = tabulate(tabla, headers=cabeceras, tablefmt="fancy_grid")
        else:
            tabla = "ninguna_tarea", None
        return tabla

    # Método para quitar una tarea
    def quitar(self, indice_tarea):
        try:
            indice_tarea = int(indice_tarea) - 1
            tarea = self.tareas[indice_tarea]
            self.tareas.remove(tarea)
            self.guardar()
            return "tarea_quitada", tarea["tarea"]
        except IndexError:
            return "tarea_no_encontrada", None
        except ValueError:
            return "numero_invalido", None


### Funciónes ###

# Codigos ANSI para resetear visualización.
resetear_pantalla = "\033[H\033[J"
resetear_linea = "\033[F\033[K"


# Mantener una visualizacion limpia y dinámica.
def visualizacion(lista_tareas, aviso=None):  # Inicializar input de aviso a None para la primera visualización de main.
    print(resetear_pantalla)
    print(f"### LISTA DE TAREAS ###\n")
    print(f"====| {date.today()} |====\n")
    if not lista_tareas.tareas:
        print(f"{Avisos.aviso('ninguna_tarea', None)}\n")
    else:
        print(f"{lista_tareas.listar()}\n")
    opciones()
    # Si se pasa un aviso a la función, imprímelo además de actualizar la tabla.
    if aviso is not None:
        print(f"\n{aviso}")
        time.sleep(1.5)


def opciones():
    # Crear diccionario de opciones
    opciones = {
        "1": "Agregar una tarea",
        "2": "Marcar una tarea como completada",
        "3": "Quitar una tarea",
        "4": "Salir",
    }
    print(f"##### Opciones #####\n")
    for opcion in opciones:
        print(f"{opcion} - {opciones[opcion]}")
    print()


def main():
    # Llamar clase lista de tareas con nombre de archivo json.
    lista_tareas = Lista_de_tareas("datos.json")

    # Bucle while permite que el programa sigue abierto hasta que se selccione la opción de salir.
    while True:
        visualizacion(lista_tareas)
        print(f"Por favor, elige una opcion (1-4): ", end="")
        seleccion = input()

        if seleccion == "1":
            opcion_agregar(lista_tareas)
        elif seleccion == "2":
            opcion_completar(lista_tareas)
        elif seleccion == "3":
            opcion_quitar(lista_tareas)
        elif seleccion == "4":
            opcion_adios()
            break
        else:
            aviso = f"{resetear_linea}{Avisos.aviso('opcion_invalida', None)}"
            visualizacion(lista_tareas, aviso)


### Opciones ###


def opcion_agregar(lista_tareas):
    while True:
        print(
            f"{resetear_linea}Introduce una tarea. Para volver atras, usa '0': ",
            end="",
        )
        nombre_tarea = input()
        # 0 termina el bucle para volver atras
        if nombre_tarea == "0":
            break
        # Si entrada es vacía, habrá un aviso y el usuario puede volver a intentar.
        elif nombre_tarea == "":
            aviso = f"{resetear_linea}{Avisos.aviso('ninguna_entrada', None)}"
            visualizacion(lista_tareas, aviso)
        # Quitar cualquier whitespace de la entrada, guardarla en la lista. Mostrar mensaje de éxito y volver.
        else:
            nombre_tarea_format = nombre_tarea.strip()
            agregada = lista_tareas.agregar(nombre_tarea_format)
            aviso = f"{resetear_linea}{Avisos.aviso(*agregada)}"
            visualizacion(lista_tareas, aviso)
            return


def opcion_completar(lista_tareas):
    # Lista de mensajes de ánimo.
    animos = [
        "¡Enhorabuena!",
        "¡Bien hecho!",
        "¡Así se hace!",
        "¡Excelente!",
        "¡Súper!",
    ]
    # Si no hay tareas en la lista, mostrar aviso y volver.
    if not lista_tareas.tareas:
        aviso = f"{resetear_linea}{Avisos.aviso('ninguna_tarea', None)}"
        visualizacion(lista_tareas, aviso)
        return

    while True:
        print(
            f"{resetear_linea}Introduce el número de la tarea completada. Para volver atras, usa '0': ",
            end="",
        )
        completada = input()
        if completada == "0":
            return
        else:
            resultado, tarea = lista_tareas.completar(completada)
            # Si el metodo devuelve el aviso no_encontrada, avisar y intentar de nuevo
            if resultado == "tarea_no_encontrada":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
            # Si el metodo devuelve el aviso numero_invalido, avisar y intentar de nuevo
            elif resultado == "numero_invalido":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
            elif resultado == "tarea_ya_completada":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
                break
            # Si la tarea aparece en la lista, marcar como completada.
            else:
                # Usar random choice para añadir un mensaje de ánimo al aviso :)
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)} {random.choice(animos)}"
                visualizacion(lista_tareas, aviso)
                break


def opcion_quitar(lista_tareas):
    # Si no hay tareas en la lista, avisar y volver atras.
    if not lista_tareas.tareas:
        aviso = f"{resetear_linea}{Avisos.aviso('ninguna_tarea', None)}"
        visualizacion(lista_tareas, aviso)
        return
    # Bucle while que permite que se intente de nuevo si el input no es valido.
    while True:
        print(
            f"{resetear_linea}Introduce el número de la tarea que quieres quitar. Para volver atras, usa '0': ",
            end="",
        )
        quitar = input()
        if quitar == "0":
            return
        else:
            # Misma funcionalidad de función completar.
            resultado, tarea = lista_tareas.quitar(quitar)
            if resultado == "tarea_no_encontrada":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
            elif resultado == "numero_invalido":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
            else:
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
                break


# Mensajes de despedida aleatorios.
def opcion_adios():
    mensajes = [
        "¡Adiós! 👋",
        "¡Hasta luego! 😊",
        "¡Nos vemos pronto! 👍",
        "¡Hasta la próxima! ✌️",
    ]
    print(f"{resetear_linea}{random.choice(mensajes)}\n")


if __name__ == "__main__":
    main()
