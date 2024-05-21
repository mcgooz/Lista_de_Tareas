# Lista de Tareas // Todo List

Lista de Tareas es un programa para apuntar y gestionar tareas.  
Lista de Tareas is a program for noting down and managing tasks.  

## Librerías // Libraries

El programa principal utiliza dos clases personalizadas, las cuales se tienen que importar desde tareaclass.py y avisos.py.  
The main program uses two custom classes, which have to be imported from tareaclass.py and avisos.py.  

```python
from avisos import Avisos
from tareaclass import ListaTareas
```

El programa principal también utiliza las librerías a continuación:
- *datetime* para mostrar la fecha.
- *random* para mostrar varios mensajes de ánimo y despedida.
- *time* para dar un momento para leer los avisos.

The main program also utilises the following libraries:
- *datetime* to show the date.
- *random* to show various messages of encouragement, and farewells.
- *time* to allow for a moment to read the notification messages.

El archivo tareaclass.py utiliza:
- *tabulate* para mostrar la lista de tareas en una tabla.
- *json* para guardar y recuperar datos en un archivo json.

The file tareaclass.py makes use of:
- *tabulate* to show the list as a formatted table.
- *json* to save and load the data in a json file.


## Uso // Usage

Con este programa, puedes agregar tareas, marcarlas como completadas y quitarlas. Tiene una visualización dinámica que actualiza después de cada operación.  
El programa utiliza JSON para persistencia de datos, que permite guardar y recuperar tareas de un archivo. Esto asegura que la lista de tareas se mantiene entre sesiones.

With this program, you can add tasks, mark them as complete and remove them. It has a dynamic display within the terminal that updates after each operation.  
The program uses JSON for data persistence, which allows it to save and load tasks from a file. This ensures that the task list is preserved between sessions.