see below for English  

## Lista de Tareas  

Un programa para apuntar y gestionar tareas.  

## Requisitos

El programa principal, lista_de_tareas.py, hace uso de los tres archivos siguientes:  
- **tareaclass.py** Una clase que contiene la lista de tareas y sus métodos correspondientes.  
- **avisos.py** y **resultados.py**: Se utilizan para definir y gestionar las notificaciones que informarán al usuario de cualquier error de entrada.  

También se utilizan las siguientes librerías:
- *datetime* para mostrar la fecha.
- *random* para mostrar mensajes aleatorios de ánimo y despedida.

```python
from avisos import Avisos
from resultados import Resultados
from tareaclass import ListaTareas
from datetime import date
import random
```

El archivo tareaclass.py hace uso de:
- Los archivos **avisos.py** y **resultados.py**.  
- *tabulate* para mostrar la lista en una tabla formateada.  
- *json* para guardar y cargar los datos de un archivo json.  

```python
from avisos import Avisos
from resultados import Resultados
from tabulate import tabular
import json
```

## Uso  

Con este programa, puedes agregar tareas, marcarlas como completadas y quitarlas. Tiene una visualización dinámica que actualiza después de cada operación.  
El programa utiliza JSON para persistencia de datos, que permite guardar y recuperar tareas de un archivo. Esto asegura que la lista de tareas se mantiene entre sesiones.

## English  
## Lista de Tareas (Todo List)  

A program for creating and managing tasks. 

## Requirements

The main program, lista_de_tareas.py, makes use of the following three files:  
- **tareaclass.py** A class that contains the list of tasks and its corresponding methods.  
- **avisos.py** and **resultados.py**: These are used to define and manage the notifications that will inform the user of any input error.  

The following libraries are also utilised:
- *datetime* to show the date.
- *random* to show randomised messages of encouragement, and farewell.

```python
from avisos import Avisos
from resultados import Resultados
from tareaclass import ListaTareas
from datetime import date
import random
```

The file tareaclass.py makes use of:
- The **avisos.py** y **resultados.py** files.  
- *tabulate* to show the list as a formatted table.  
- *json* to save and load the data in a json file.  

```python
from avisos import Avisos
from resultados import Resultados
from tabulate import tabulate
import json
```

## Usage

With this program, you can add tasks, mark them as complete and remove them. It has a dynamic display within the terminal that updates after each operation.  
The program uses JSON for data persistence, which allows it to save and load tasks from a file. This ensures that the task list is preserved between sessions.
