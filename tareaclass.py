from avisos import Avisos
from resultados import Resultados
from tabulate import tabulate
import json


class ListaTareas:

    def __init__(self):
        self.lista = []
        self.cargar()

    # Recuperar tareas guardadas.
    def cargar(self):
        try:
            with open("datos.json", "r") as archivo:
                datos = json.load(archivo)
                self.lista = datos
        # Si el json aun no se ha creado (o no se puede abrir), inicializar una lista nueva.
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []

    # Guardar cambios al json.
    def guardar(self):
        with open("datos.json", "w") as archivo:
            json.dump(self.lista, archivo, indent=4)
    
    # Agregar una nueva tarea a la lista.
    def agregar(self, tarea):
        for entrada in self.lista:
            if entrada["tarea"] == tarea:
                return Resultados.TAREA_YA_EXISTE, tarea["tarea"]

        self.lista.append({"tarea": tarea, "completada": False})
        self.guardar()
        return Resultados.TAREA_AGREGADA, tarea

    # Marcar una tarea como completada.
    def completar(self, i):
        try:
            entrada = int(i) - 1
            tarea = self.lista[entrada]
            if tarea["completada"]:
                    return Resultados.TAREA_YA_COMPLETADA, tarea["tarea"]
            else:
                tarea["completada"] = True
                self.guardar()
                return Resultados.TAREA_COMPLETADA, tarea["tarea"]
        except IndexError:
            return Resultados.TAREA_NO_ENCONTRADA, None
        except ValueError:
            return Resultados.NUMERO_INVALIDO, None

    # Quitar una tarea de la lista.    
    def quitar(self, i):
        try:
            entrada = int(i) - 1
            tarea = self.lista[entrada]
            self.lista.remove(tarea)
            self.guardar()
            return Resultados.TAREA_QUITADA, tarea["tarea"]
        except IndexError:
            return Resultados.TAREA_NO_ENCONTRADA, None
        except ValueError:
            return Resultados.NUMERO_INVALIDO, None

    # Seguir el estado de una tarea. 
    def estado(self, tarea):
        # Definir colores con códigos de ANSI.
        verde = "\033[92m"
        azul = "\033[94m"
        negro = "\033[0m"  # Resetear color
        if not tarea["completada"]:
            return (azul + "Pendiente" + negro)
        elif tarea["completada"]:
            return (verde + "Completada" + negro)

    # Crear y formatear la lista.
    def tabular(self):
        tabla = []
        encabezados = ["#", "Tarea", "Estado"]
        for indice, tarea in enumerate(self.lista, start=1):
            estado = self.estado(tarea)
            tabla.append([indice, tarea["tarea"], estado])
        tabla = tabulate(tabla, headers=encabezados, tablefmt="fancy_grid")
        return tabla
