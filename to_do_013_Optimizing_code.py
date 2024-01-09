while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()

  if 'add' in user_action:
    todo = user_action[4:] 
    todo = todo + "\n"

    #context manager
    with open(r'.../todos.txt', 'r') as file:
      todos = file.readlines()

    todos.append(todo)
    
    with open(r'.../todos.txt', 'w') as file:
      file.writelines(todos)

  elif 'show' in user_action: 

    with open(r'.../todos.txt', 'r') as file:
      todos = file.readlines()

    for index, i in enumerate(todos): 
      i = i.strip('\n')
      row = f"{int(index)+1}.{i.title()}"
      print(row)

  elif 'edit' in user_action:
    number = int(user_action[5:])
    number = number - 1
    #Open the txt file 
    with open(r'.../todos.txt', 'r') as file:
      todos = file.readlines()

    new_todo = input("Enter a new to do: ")
    todos[number] = new_todo + '\n' 
    
    with open(r'.../todos.txt', 'w') as file:
      file.writelines(todos)
  
  elif 'complete' in user_action:
    complete = int(user_action[9:])

    with open(r'.../todos.txt', 'r') as file:
      todos = file.readlines()
    
    completed = complete - 1
    removed = todos[completed].strip('\n') #.strip('\n') to remove the break from the message
    todos.pop(completed)

    with open(r"C:\Users\leona\OneDrive\Escritorio\Python Mega Course Build 20 Apps\app01_to_do_app\todos.txt", 'w') as file:
      file.writelines(todos)

    message = f"Todo {removed} was removed from the list"
    print(message)

  elif 'exit' in user_action:
    break

  else:
    print("Command is not valid")

print("Have a nice day!")
