#todos = [] deleted since we will work with txt files

while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()
  
  match user_action:
    case 'add':
      todo = input("Enter a to do: ") + "\n"

      #context manager
      with open('/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'r') as file:
        todos = file.readlines()

      todos.append(todo)
     
      with open('/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'w') as file:
        file.writelines(todos)

    case 'show': 

      with open('/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'r') as file:
        todos = file.readlines()

      for index, i in enumerate(todos): 
        i = i.strip('\n')
        row = f"{int(index)+1}.{i.title()}"
        print(row)

    case 'edit':
      number = int(input("Number of the todo to edit: "))
      number = number - 1
      #Open the txt file 
      with open('/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'r') as file:
        todos = file.readlines()

      new_todo = input("Enter a new to do: ")
      todos[number] = new_todo + '\n' 
      
      with open('/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'w') as file:
        file.writelines(todos)
    
    case 'complete':
      complete = input("Enter the number of the completed to do: ")

      with open('/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'r') as file:
        todos = file.readlines()
      
      completed = int(complete) - 1
      removed = todos[completed].strip('\n') #.strip('\n') to remove the break from the message
      todos.pop(completed)

      with open('/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'w') as file:
        file.writelines(todos)

      message = f"Todo {removed} was removed from the list"
      print(message)

    case 'exit':
      break
    
    case x:
      print("You entered a wrong command")

print("Have a nice day!")