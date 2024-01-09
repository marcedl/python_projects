while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()

  if user_action.startswith("add"):
    todo = user_action[4:] 
    todo = todo + "\n"

    #context manager
    with open(r'.../todos.txt', 'r') as file:
      todos = file.readlines()

    todos.append(todo)
    
    with open(r'.../todos.txt', 'w') as file:
      file.writelines(todos)

  elif user_action.startswith("show"): 

    with open(r'.../todos.txt', 'r') as file:
      todos = file.readlines()

    for index, i in enumerate(todos): 
      i = i.strip('\n')
      row = f"{int(index)+1}.{i.title()}"
      print(row)

  elif  user_action.startswith("edit"):
    try:
      number = int(user_action[5:])
      number = number - 1
      #Open the txt file 
      with open(r'.../todos.txt', 'r') as file:
        todos = file.readlines()

      new_todo = input("Enter a new to do: ")
      todos[number] = new_todo + '\n' 
      
      with open(r'.../todos.txt', 'w') as file:
        file.writelines(todos)
    except ValueError:
      print("Your command is not valid")
      continue
  
  elif  user_action.startswith("complete"):
    try:
      complete = int(user_action[9:])

      with open(r'.../todos.txt', 'r') as file:
        todos = file.readlines()
      
      completed = complete - 1
      removed = todos[completed].strip('\n') #.strip('\n') to remove the break from the message
      todos.pop(completed)

      with open(r'.../todos.txt', 'w') as file:
        file.writelines(todos)

      message = f"Todo {removed} was removed from the list"
      print(message)
    except IndexError:
      print("There is no item with that number")

  elif user_action.startswith("exit"):
    break

  else:
    print("Command is not valid")

print("Have a nice day!")
