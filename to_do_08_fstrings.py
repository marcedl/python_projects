todos = []

while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()
  
  match user_action:
    case 'add':
      todo = input("Enter a to do: ")
      todos.append(todo)
    case 'show': # 'show' | 'display' .... "|"" symbol means or
      for index, i in enumerate(todos): #enumerate is a function
        #print(int(index) + 1, i) change this for a f string
        row = f"{int(index)+1}.{i.title()}"
        print(row)
    case 'edit':
      number = int(input("Number of the todo to edit: "))
      number = number - 1
      neggsew_todo = input("Enter a new to do: ")
      todos[number] = new_todo
    case 'complete':
      complete = input("Enter the number of the completed to do: ")
      complete = int(complete) - 1
      new_list = todos.pop(complete)
    case 'exit':
      break
    case x: #adding an anynomous variable will match with any other input added by the user
      print("You entered a wrong command")

print("Have a nice day!")