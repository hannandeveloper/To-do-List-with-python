user_task = []


def add():   
       todo = input(f"{i}.Enter a task: ")
       user_task.append(todo)
       return user_task
    


def view():
   if not user_task:
        print("noo task")
   else:
        for i,task in enumerate(user_task,1):
             print(f"{task}")

def delete():
    try:
        a = int(input("Enter the index of which task you wnat to delete :\t"))
        try:
          user_task.pop(a-1)
        except IndexError:
            print("--------------> no value exists in this index")

    except ValueError:
        print("--------------> Enter a value")



while True:
    user_choice = input("Enter your choice: \nadd 1 view 2 delete 3 exit 4 :\t")
    if user_choice =="1" :
         try:
           num_task = int(input("how many task you want to enter: "))
           num_task+=1
           for i in range(1,num_task):
                add()
         except ValueError:
             print("--------------> enter a num ")
    elif user_choice == "2":
        view()
    elif user_choice == "3":
        delete()
    elif user_choice == "4":
        break
    else:
         print("--------------> Enter num according to the instruction")