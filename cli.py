#from functions import get_todos,write_todos
import functions
import time

status=time.strftime("%b %d,%Y %H-%M-%S")
print(f"It is{status}")
while True:
    user_action=input("Type add,show,edit,complete or exit")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo=user_action[4:]+"\n"
        todos=functions.get_todos()
        todos.append(todo)#append can be applied on list only and not on string
        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos=functions.get_todos()
        new_todos=[]
        for item in todos:
            new_item=item.strip('\n')
            new_todos.append(new_item)
        for index,item in enumerate(new_todos):
            item=item.title()
            item=f"{index+1}-{item}"
            print(item)
    elif user_action.startswith("edit"):
        try:#error handling
            number=int(user_action[5:])
            number=number-1
            new_todo=input("Enter the new todo:")+"\n"
            todos=functions.get_todos()
            if number<=(int(len(todos))):
                todos[number]=new_todo
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not Valid")
    elif user_action.startswith("complete"):
        try:#error handling
            todos=functions.get_todos()
            number = int(user_action[9:])
            number = number - 1
            if number <= (int(len(todos))):
                todos.remove(todos[number])
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
    elif user_action.startswith("exit"):
        break
    else:
        print("Incorrect Command")

print("Bye!")


