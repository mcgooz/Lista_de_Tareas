from avisos import Avisos
from tareaclass import ListaTareas
from datetime import date
import random
import time


# Codigos ANSI para resetear visualización.
resetear_pantalla = "\033[H\033[J"
resetear_linea = "\033[F\033[K"

# Instanciar la clase.
lista_tareas = ListaTareas()

# Mantener una visualización limpia y dinámica.
def visualizacion(lista_tareas, aviso=None):  # Inicializar input de aviso a None para la visualización inicial.
    print(resetear_pantalla)
    print(f"### LISTA DE TAREAS ###\n")
    print(f"====| {date.today()} |====\n")

    # Si no hay entradas, imprimir aviso de ninguna tarea.
    if not lista_tareas.lista:
        print(f"{Avisos.aviso('ninguna_tarea', None)}\n")
    else:
        print(f"{lista_tareas.tabular()}\n")
    opciones()

    # Imprimir aviso correspondiente.
    if aviso is not None:
        print(f"\n{aviso}")
        time.sleep(1.5) # Una pausa corta para leer el aviso.

def opciones():
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
    intro = ((
        "\n"
        "=============================================< INFORMACIÓN >=============================================\n"
        "------\n"
        "<<< Se recomienda maximizar el terminal para asegurar una experiencia optima >>>\n"
        "------\n"
        "<<<<< Por favor, ten en cuenta que el siguiente paso limpiará cualquier texto visible del terminal >>>>> \n"
        "------\n"
        "=========================================================================================================\n"
))
    # Calcular longitud de la linea más larga para justificar texto al centro.
    centrar = max(len(line) for line in intro.split('\n'))
    for line in intro.split('\n'):
        print(line.center(centrar))
    input("Por favor, pulsa Enter para continuar...\n")

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
        print(f"{resetear_linea}Introduce una tarea. Para volver atras, usa '0': ", end="")
        nombre_tarea = input()
        # 0 rompe del bucle para volver atras.
        if nombre_tarea == "0":
            break
        # Si la entrada está vacía, se avisa y el usuario puede volver a intentar.
        elif nombre_tarea == "":
            aviso = f"{resetear_linea}{Avisos.aviso('ninguna_entrada', None)}"
            visualizacion(lista_tareas, aviso)
        else:
            tarea_formatada = nombre_tarea.strip() # Quitar whitespace de la entrada.
            agregada = lista_tareas.agregar(tarea_formatada)
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
    # Si no hay tareas en la lista, avisar y volver.
    if not lista_tareas.lista:
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
            # Si el resultado es no_encontrada, avisar y intentar de nuevo.
            if resultado == "tarea_no_encontrada":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
            # Si el resultado es numero_invalido, avisar y intentar de nuevo.
            elif resultado == "numero_invalido":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
            # Si la tarea ya ha sido marcada como completada, avisar y volver a la pantalla principal.
            elif resultado == "tarea_ya_completada":
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)}"
                visualizacion(lista_tareas, aviso)
                break
            else:
                # Utilizar random choice para añadir un mensaje de ánimo al aviso :)
                aviso = f"{resetear_linea}{Avisos.aviso(resultado, tarea)} {random.choice(animos)}"
                visualizacion(lista_tareas, aviso)
                break


def opcion_quitar(lista_tareas):
    # Si no hay tareas en la lista, avisar y volver atras.
    if not lista_tareas.lista:
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


# Mensajes de despedida randomizados.
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