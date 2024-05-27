from avisos import Avisos
from resultados import Resultados
from tareaclass import ListaTareas
from datetime import date
import random


# Variables globales de ANSI para restablecer visualización.
RESETEAR_PANTALLA = "\033[H\033[J"
RESETEAR_LINEA = "\033[F\033[K"

# Instanciar la clase y cargar lista guardada (si existe).
lista_tareas = ListaTareas()
lista_tareas.cargar()


# Formular mensajes de aviso.
def crear_aviso(resultado, *args, animo=None):
    mensaje = Avisos.aviso(resultado, *args)
    if animo is not None:
        mensaje += " " + animo
    aviso = f"{RESETEAR_LINEA}{mensaje}"
    visualizacion(lista_tareas, aviso)


# Mantener una visualización limpia y dinámica.
def visualizacion(lista_tareas, aviso=None):
    print(RESETEAR_PANTALLA)
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
        input("Pulsa Enter para continuar...")
        print(RESETEAR_LINEA, end="")


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
    intro = (
        "\n"
        "=============================================< INFORMACIÓN >=============================================\n"
        "------\n"
        "<<< Se recomienda maximizar el terminal para asegurar una experiencia óptima >>>\n"
        "------\n"
        "<<<<< Por favor, ten en cuenta que el siguiente paso limpiará cualquier texto visible del terminal >>>>> \n"
        "------\n"
        "=========================================================================================================\n"
    )
    # Calcular longitud de la linea más larga para justificar el texto al centro.
    centrar = max(len(line) for line in intro.split("\n"))
    for line in intro.split("\n"):
        print(line.center(centrar))
    input("Pulsa Enter para continuar...\n")

    # Bucle while permite que el programa siga abierto hasta que se selccione la opción de salir.
    while True:
        visualizacion(lista_tareas, aviso=None)
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
            crear_aviso(Resultados.OPCION_INVALIDA, None)


### Opciones ###

def opcion_agregar(lista_tareas):
    while True:
        print(
            f"{RESETEAR_LINEA}Introduce una tarea. Para volver atras, usa '0': ", end=""
        )
        nombre_tarea = input()
        nombre = nombre_tarea.strip()

        # 0 rompe del bucle para volver atras.
        if nombre == "0":
            break
        # Si la entrada está vacía, se avisa al usuario para que vuelva a intentar.
        elif nombre == "":
            crear_aviso(Resultados.NINGUNA_ENTRADA, None)
        elif nombre == lista_tareas.check(nombre):
            crear_aviso(Resultados.TAREA_YA_EXISTE, nombre)
        else:
            lista_tareas.agregar(nombre)
            crear_aviso(Resultados.TAREA_AGREGADA, nombre)
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
        crear_aviso(Resultados.NINGUNA_TAREA, None)
        return
    
    # Si todas las tareas listadas ya están completadas, avisar y volver.
    elif lista_tareas.terminado():
        crear_aviso(Resultados.TODAS_COMPLETADAS, None)
        return

    while True:
        print(
            f"{RESETEAR_LINEA}Introduce el número de la tarea completada. Para volver atras, usa '0': ",
            end="",
        )
        completada = input()
        if completada == "0":
            return
        else:
            resultado, tarea = lista_tareas.completar(completada)
            # Si el resultado es no_encontrada, avisar y intentar de nuevo.
            if resultado == Resultados.TAREA_NO_ENCONTRADA:
                crear_aviso(resultado, None)
            # Si el resultado es numero_invalido, avisar y intentar de nuevo.
            elif resultado == Resultados.NUMERO_INVALIDO:
                crear_aviso(resultado, None)
            # Si la tarea ya ha sido marcada como completada, avisar.
            elif resultado == Resultados.TAREA_YA_COMPLETADA:
                crear_aviso(resultado, tarea)
                if lista_tareas.terminado():
                    break
            else:
                # Utilizar random choice para añadir un mensaje de ánimo al aviso :)
                resultado = Resultados.TAREA_COMPLETADA
                animo = random.choice(animos)
                crear_aviso(resultado, tarea, animo=animo)
                if lista_tareas.terminado():
                    break


def opcion_quitar(lista_tareas):
    # Si no hay tareas en la lista, avisar y volver atras.
    if not lista_tareas.lista:
        crear_aviso(Resultados.NINGUNA_TAREA, None)
        return
    # Bucle while que permite que se intente de nuevo si el input no es valido.
    while True:
        print(
            f"{RESETEAR_LINEA}Introduce el número de la tarea que quieres quitar. Para volver atras, usa '0': ",
            end="",
        )
        quitar = input()
        if quitar == "0":
            return
        else:
            resultado, tarea = lista_tareas.quitar(quitar)
            if resultado == Resultados.TAREA_NO_ENCONTRADA:
                crear_aviso(resultado, None)
            elif resultado == Resultados.NUMERO_INVALIDO:
                crear_aviso(resultado, None)
            else:
                crear_aviso(Resultados.TAREA_QUITADA, tarea)
                if lista_tareas.lista:
                    continue
                else:
                    break


# Mensajes de despedida randomizados.
def opcion_adios():
    mensajes = [
        "¡Adiós! 👋",
        "¡Hasta luego! 😊",
        "¡Nos vemos pronto! 👍",
        "¡Hasta la próxima! ✌️",
    ]
    print(f"{RESETEAR_LINEA}{random.choice(mensajes)}\n")


if __name__ == "__main__":
    main()
