from avisos import Avisos
from resultados import Resultados
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
def visualizacion(lista_tareas, aviso = None):
    print(resetear_pantalla)
    print(f"### LISTA DE TAREAS ###\n")
    print(f"====| {date.today()} |====\n")

    # Si no hay entradas, imprimir aviso de ninguna tarea.
    if not lista_tareas.lista:
        print(f"{Avisos.aviso(Resultados.NINGUNA_TAREA, None)}\n")
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
    input("Pulsa Enter para continuar...\n")

    # Bucle while permite que el programa sigue abierto hasta que se selccione la opción de salir.
    while True:
        visualizacion(lista_tareas, aviso = None)
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
            aviso = f"{resetear_linea}{Avisos.aviso(Resultados.OPCION_INVALIDA, None)}"
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
            aviso = f"{resetear_linea}{Avisos.aviso(Resultados.NINGUNA_ENTRADA, None)}"
            visualizacion(lista_tareas, aviso)
        else:
            tarea_formatada = nombre_tarea.strip() # Quitar whitespace de la entrada.
            lista_tareas.agregar(tarea_formatada)
            aviso = f"{resetear_linea}{Avisos.aviso(Resultados.TAREA_AGREGADA, tarea_formatada)}"
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
        aviso = f"{resetear_linea}{Avisos.aviso(Resultados.NINGUNA_TAREA, None)}"
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
            if resultado == Resultados.TAREA_NO_ENCONTRADA:
                aviso = f"{resetear_linea}{Avisos.aviso(Resultados.TAREA_NO_ENCONTRADA, None)}"
                visualizacion(lista_tareas, aviso)
            # Si el resultado es numero_invalido, avisar y intentar de nuevo.
            elif resultado == Resultados.NUMERO_INVALIDO:
                aviso = f"{resetear_linea}{Avisos.aviso(Resultados.NUMERO_INVALIDO, None)}"
                visualizacion(lista_tareas, aviso)
            # Si la tarea ya ha sido marcada como completada, avisar y volver a la pantalla principal.
            elif resultado == Resultados.TAREA_YA_COMPLETADA:
                aviso = f"{resetear_linea}{Avisos.aviso(Resultados.TAREA_YA_COMPLETADA, tarea)}"
                visualizacion(lista_tareas, aviso)
                break
            else:
                # Utilizar random choice para añadir un mensaje de ánimo al aviso :)
                aviso = f"{resetear_linea}{Avisos.aviso(Resultados.TAREA_COMPLETADA, tarea)} {random.choice(animos)}"
                visualizacion(lista_tareas, aviso)
                break


def opcion_quitar(lista_tareas):
    # Si no hay tareas en la lista, avisar y volver atras.
    if not lista_tareas.lista:
        aviso = f"{resetear_linea}{Avisos.aviso(Resultados.NINGUNA_TAREA, None)}"
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
            if resultado == Resultados.TAREA_NO_ENCONTRADA:
                aviso = f"{resetear_linea}{Avisos.aviso(Resultados.TAREA_NO_ENCONTRADA, None)}"
                visualizacion(lista_tareas, aviso)
            elif resultado == Resultados.NUMERO_INVALIDO:
                aviso = f"{resetear_linea}{Avisos.aviso(Resultados.NUMERO_INVALIDO, None)}"
                visualizacion(lista_tareas, aviso)
            else:
                aviso = f"{resetear_linea}{Avisos.aviso(Resultados.TAREA_QUITADA, tarea)}"
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