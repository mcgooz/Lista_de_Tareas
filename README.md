see below for English  

## Lista de Tareas  

Un programa para apuntar y gestionar tareas.  

## Librerías  

El programa principal, lista_de_tareas, utiliza los siguientes tres archivos:  
- **tareaclass.py**: una clase que contiene la lista de tareas y sus métodos correspondientes.  
- **avisos.py** y **resultados.py**: definen los mensajes de aviso para informar al usuario de cualquier (casi) error.  

```python
from avisos import Avisos
from resultados import Resultados
from tareaclass import ListaTareas
```

También se utiliza las librerías a continuación:
- *datetime* para mostrar la fecha.
- *random* para mostrar varios mensajes de ánimo y despedida.
- *time* para dar un momento para leer los avisos.

El archivo tareaclass.py utiliza:
- *tabulate* para mostrar la lista de tareas en una tabla.
- *json* para guardar y recuperar datos en un archivo json.


## Uso  

Con este programa, puedes agregar tareas, marcarlas como completadas y quitarlas. Tiene una visualización dinámica que actualiza después de cada operación.  
El programa utiliza JSON para persistencia de datos, que permite guardar y recuperar tareas de un archivo. Esto asegura que la lista de tareas se mantiene entre sesiones.

# English
## Lista de Tareas (Todo List)  

A program for creating and managing tasks.  

## Libraries  

The main program, lista_de_tareas, makes use of the following three files:  
- **tareaclass.py** A class that contains the list of tasks and its corresponding methods.  
- **avisos.py** and **resultados.py**: These define the notifications that will inform the user of (almost) any error.  

```python
from avisos import Avisos
from resultados import Resultados
from tareaclass import ListaTareas
```

The following libraries are also utilised:
- *datetime* to show the date.
- *random* to show various messages of encouragement, and farewells.
- *time* to allow for a moment to read the notification messages.

The file tareaclass.py makes use of:
- *tabulate* to show the list as a formatted table.
- *json* to save and load the data in a json file.


## Usage

With this program, you can add tasks, mark them as complete and remove them. It has a dynamic display within the terminal that updates after each operation.  
The program uses JSON for data persistence, which allows it to save and load tasks from a file. This ensures that the task list is preserved between sessions.
