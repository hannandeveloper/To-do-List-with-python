user_task = []

def add():
    todo = input("Enter a task: ")
    user_task.append(todo)
    return user_task


def view():
   for task in user_task:
       print(f"{task}")

def delete():
    try:
        a = int(input("Enter the index of which task you wnat to delete"))
        user_task.pop(a)
    except ValueError:
        print("Enter a value")



add()
view()
delete()
print(user_task)