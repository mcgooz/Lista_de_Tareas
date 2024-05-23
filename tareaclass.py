from avisos import Avisos
from resultados import Resultados
from tabulate import tabulate
import json


class ListaTareas:
    """Gestionar una lista de tareas."""

    def __init__(self):
        """Inicializar una instancia de ListaTareas con una lista vacía."""
        self.lista = []

    def cargar(self):
        """Recuperar tareas guardadas del json. 
        
        Si el json aun no existe o no se puede abrir, inicializar una lista nueva.
        """
        try:
            with open("datos.json", "r") as archivo:
                datos = json.load(archivo)
                self.lista = datos
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista = []

    def guardar(self):
        """Guardar cualquier cambio al archivo json."""
        with open("datos.json", "w") as archivo:
            json.dump(self.lista, archivo, indent=4)
    
    def agregar(self, entrada):
        """Agregar una nueva tarea a la lista.
        
        Por defecto, una tarea se agregará con el estado 'completada' como False.
        Luego, guardar la entrada en el json.

        Args:
            tarea (str): La tarea a agregar.

        Returns:
            tuple: Resultado de la operación y la tarea.
        """

        self.lista.append({"tarea": entrada, "completada": False})
        self.guardar()
        return Resultados.TAREA_AGREGADA, entrada
    
    def check(self, tarea):
        """Buscar una tarea por nombre. Si una tarea ya existe en la lista, devolver un mensaje de aviso para no duplicarla."""

        for entrada in self.lista:
            if entrada["tarea"] == tarea:
                return tarea
        return None

    def completar(self, i):
        """Marcar una tarea como completada.
        
        Si una tarea ya está completada, devolver un aviso de esto mismo.
        Si no, cambiar 'completada' a True y guardar el cambio en el json.
        Si una tarea no existe o la entrada no es válida, devolver el aviso correspondiente.

        Args:
            i (int): Índice de la tarea a completar.

        Returns:
            tuple: Resultado de la operación y la tarea o None.
        """
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
   
    def quitar(self, i):
        """Quitar una tarea de la lista y guardar el cambio en el json.
        
        Si una tarea no existe o la entrada no es válida, devolver el aviso correspondiente.

        Args:
            i (int): Índice de la tarea a quitar.

        Returns:
            tuple: Resultado de la operación y la tarea o None.
        """
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
 
    def estado(self, tarea):
        """Obtener el estado de una tarea formateado con colores ANSI.
        
        Args:
            tarea (dict): La tarea cuyo estado se quiere obtener.

        Returns:
            str: El estado formateado de la tarea.
        """

        # Definir colores con códigos de ANSI.
        verde = "\033[92m"
        azul = "\033[94m"
        negro = "\033[0m"  # Resetear color
        if not tarea["completada"]:
            return (azul + "Pendiente" + negro)
        elif tarea["completada"]:
            return (verde + "Completada" + negro)

    def tabular(self):
        """Crear y formatear la lista de tareas en una tabla.
        
        Returns:
            str: La tabla formateada.
        """
        tabla = []
        encabezados = ["#", "Tarea", "Estado"]
        for indice, tarea in enumerate(self.lista, start=1):
            estado = self.estado(tarea)
            tabla.append([indice, tarea["tarea"], estado])
        tabla = tabulate(tabla, headers=encabezados, tablefmt="fancy_grid")
        return tabla
