from resultados import Resultados

class Avisos:
    """Proporcionar mensajes de aviso basados en resultados de operaciones en ListaTareas."""

    @staticmethod
    def aviso(clave, *args):
        """Devolver un mensaje de aviso correspondiente.
        
        Args:
            clave (Resultados): La clave del resultado de la operación.
            *args: Argumentos adicionales que se incluirán en el mensaje de aviso.
        
        Returns:
            str: El mensaje de aviso correspondiente.
        """

        mensajes = {
            Resultados.TAREA_AGREGADA: f"¡La tarea '{args[0]}' se ha agregado con éxito!",
            Resultados.TAREA_YA_EXISTE: f"La tarea '{args[0]}' ya existe.",
            Resultados.TAREA_COMPLETADA: f"¡La tarea '{args[0]}' ha sido marcada como completada!",
            Resultados.TAREA_YA_COMPLETADA: f"La tarea '{args[0]}' ya está completada.",
            Resultados.TAREA_QUITADA: f"¡La tarea '{args[0]}' se ha quitado con éxito!",
            Resultados.TAREA_NO_ENCONTRADA: f"No se puede encontrar esta tarea.",
            Resultados.NUMERO_INVALIDO: f"Por favor, introduce un número.",
            Resultados.NINGUNA_TAREA: f"No hay ninguna tarea en la lista.",
            Resultados.NINGUNA_ENTRADA: f"No se ha introducido ninguna palabra.",
            Resultados.OPCION_INVALIDA: f"* Por favor, elige una opción válida (1-4). *",
        }
        return mensajes.get(clave, "")