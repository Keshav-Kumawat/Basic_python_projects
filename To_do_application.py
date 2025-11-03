
task = []
def todo():
    """ we are building To-do-application"""

    print("Welcome to the TASK MANAGER...................")
    print("1.Add a task")
    print("2.view all task")
    print("3.mark task as completed")
    print("4.delete whick task")
    print("5.exit the task")
    print("-----------------------------------------------")

def add_task():
    add = input("enter the task : ").strip()

    if add:
        task.append({"description": add , "done":False})
        print(f" task '{add}' is added.")
    else:
        print("task cannot be empty")    

def view_task():
    if not task:
        print("your to_do list is empty!!")
    else:
        for index,t in enumerate(task,start=1):
            status = "✓" if t["done"] else []
            print(f"{index}.{status} {t['description']}")

def get_task_number():
    try:
        t = int(input("Enter an task number: "))
        ind = t-1

        if 0<= ind < len(task):
            return ind
        else:
            print("invalid task number!!")
    
    except ValueError as e :
        print(f"Please! enter an valid integer!!!!!!: {e}")
    except :
        print(e) 


def mark_task_completed():
    if not task:
        print("there is no task to mark")

    view_task()
    index = get_task_number()


    if index is not None:
        if task[index]["done"]:
            print(f"task '{task[index]['description']}' is already completed.")

        else:
            task[index]["done"] = True
            print(f"task {task[index]['description']} is completed.")  

def delete_task():
    if not task:
        print("There is no task to remove")
     
    view_task()
    index = get_task_number()

    if index is not None:
        removed = task.pop(index)
        print(f" task {removed['description']} has been deleted.") 


def main():

   while True :
       todo()
       choice = input("Enter the choices between (1-5):")


       if choice == '1':
        add_task()
       elif choice == '2':
        view_task()
       elif choice == '3':
        mark_task_completed()
       elif choice == '4':
        delete_task()
       elif choice == '5':
        print("you exit the task")
        break 
       else:
        print("Invalid choice. Please enter a number between 1 and 5.")
       

if __name__=='__main__':
    main()
                













