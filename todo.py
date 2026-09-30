user_task = []

def add():
    todo = input("Enter a task: ")
    user_task.append(todo)
    return user_task


def view():
   if not user_task:
        print("noo task")
   else:
        for i,task in enumerate(user_task,1):
             print(f"{i}.{task}")

def delete():
    try:
        a = int(input("Enter the index of which task you wnat to delete :\t"))
        user_task.pop(a-1)
    except ValueError:
        print("Enter a value")



while True:
    user_choice = int(input("Enter your choice: \n add 1 view 2 delete 3 exit 4 :\t"))
    if user_choice == 1:
        add()
    elif user_choice == 2:
        view()
    elif user_choice == 3:
        delete()
    elif user_choice == 4:
        break
