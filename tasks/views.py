from django.shortcuts import render, redirect
from datetime import datetime

# In-memory list to store tasks
tasks = []

# Index view to display tasks sorted by due date
def index(request):
    sorted_tasks = sorted(tasks, key=lambda x: x['due_date'])
    return render(request, 'tasks/index.html', {'tasks': sorted_tasks})

# Add task view
def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        # Convert string to datetime
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date()

        task = {'description': description, 'due_date': due_date, 'completed': False}
        tasks.append(task)
        return redirect('index')

    return render(request, 'tasks/add_task.html')

# Mark task as completed
def mark_completed(request, id):
    task = tasks[id]
    task['completed'] = True
    return redirect('index')

# Delete task
def delete_task(request, id):
    tasks.pop(id)
    return redirect('index')
