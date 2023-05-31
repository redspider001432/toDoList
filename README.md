# ToDoList Project
This is a simple ToDoList application built with Django.

### Installation
1. Clone the repository:
```git clone https://github.com/redspider001432/toDoList.git```
2. Navigate to the project directory:
```cd toDoList```
3. Create a virtual environment (optional, but recommended):
```python -m venv myenv```
```source myenv/bin/activate```
4. Install the project dependencies:
``` pip install -r requiments.txt```
5. Apply database migrations:
``` python manage.py migrate```
6. Start the development server:
``` python manage.py runserver```
7. Access the application in your web browser at http://localhost:8000.

## Usage
* To create a new ToDo item, click on the "Add Task" button on the homepage and fill in the required information.
* To view details of a specific ToDo item, click on its title in the task list.
* To update a ToDo item, click on the "Edit" button on the task detail page and make the desired changes.
* To delete a ToDo item, click on the "Delete" button on the task detail page.

## API Endpoints
#### The project provides the following REST API endpoints:
* GET /api/tasks/ - Retrieve a list of all tasks.
* POST /api/tasks/create/ - Create a new task.
* GET /api/tasks/{task_id}/ - Retrieve details of a specific task.
* PUT /api/tasks/{task_id}/update/ - Update a task.
* DELETE /api/tasks/{task_id}/delete/ - Delete a task.
