user_task = []

def add():
    todo = input("Enter a task: ")
    user_task.append(todo)
    return user_task


def view():
   for task in user_task:
       print(f"{task}")





add()
view()