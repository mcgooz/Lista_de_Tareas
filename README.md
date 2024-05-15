# Lista de Tareas // Todo List

Lista de Tareas es un programa para apuntar tareas.  
Lista de Tareas is a program for noting down tasks.  

## Librerías // Libraries

Es necesario importar la lista de avisos desde avisos.py.  
It's necessary to import the notifications list from avisos.py.  

```python
from avisos import Avisos
```

El programa también utiliza las librerías a continuación:
- *datetime* para mostrar la fecha. 
- *tabulate* para mostrar la lista de tareas en una tabla.
- *json* para guardar y recuperar datos en un archivo json. 
- *random* para mostrar varios mensajes de ánimo y despedida.
- *time* para dar un momento para leer los avisos.

The program also utilises the following libraries:
- *datetime* to show the date. 
- *tabulate* to show the list as a formatted table.
- *json* to save and load the data in a json file.
- *random* to show various messages of encouragement, and farewells.
- *time* to allow for a moment to read the notification messages.

## Uso // Usage

Con este programa, puedes agregar tareas, marcarlas como completadas y quitarlas. Tiene una visualización dinámica en el terminal que actualiza después de cada operación.  
Creará y utilizará un archivo json para guardar la lista para que puedas salir del programa y volver a abrirlo sin perder los datos.

With this program, you can add tasks, mark them as complete and remove them. It has a dynamic display within the terminal that updates after each operation.  
It will create and use a json file to save the list so that you can quit the program and re-open it without losing any data.