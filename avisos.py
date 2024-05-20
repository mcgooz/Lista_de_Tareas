# avisos.py

class Avisos:
    @staticmethod
    def aviso(clave, *args):
        mensajes = {
            "tarea_agregada": f"¡La tarea '{args[0]}' se ha agregado con éxito!",
            "tarea_ya_existe": f"La tarea '{args[0]}' ya existe.",
            "tarea_completada": f"¡La tarea '{args[0]}' ha sido marcada como completada!",
            "tarea_ya_completada": f"La tarea '{args[0]}' ya está completada.",
            "tarea_quitada": f"¡La tarea '{args[0]}' se ha quitado con éxito!",
            "tarea_no_encontrada": f"No se puede encontrar esta tarea.",
            "numero_invalido": "Por favor, introduce un número.",
            "ninguna_tarea": "No hay ninguna tarea en la lista.",
            "ninguna_entrada": "No se ha introducido ninguna palabra.",
            "opcion_invalida": "*** Por favor, elige una opción válida. ***",
        }
        return mensajes.get(clave, "")
