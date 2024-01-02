#todos = [] deleted since we will work with txt files

while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()
  
  match user_action:
    case 'add':
      todo = input("Enter a to do: ") + "\n"
      file = open(r'/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'r') #first read the file
      todos = file.readlines() #file.read() for strings, readlines for list format
      file.close()
      
      todos.append(todo)
      
      file = open(r'/Users/marcela/Documents/Cursos/Python Mega Course Build 20 Apps/app01_to_do_app/todos.txt', 'w') #then overwrite the file
      file.writelines(todos) #file.write for strings
      file.close()
    case 'show': 
      for index, i in enumerate(todos): 
        row = f"{int(index)+1}.{i.title()}"
        print(row)
    case 'edit':
      number = int(input("Number of the todo to edit: "))
      number = number - 1
      neggsew_todo = input("Enter a new to do: ")
      new_todo = todos[number] 
    case 'complete':
      complete = input("Enter the number of the completed to do: ")
      complete = int(complete) - 1
      new_list = todos.pop(complete)
    case 'exit':
      break
    case x:
      print("You entered a wrong command")

print("Have a nice day!")