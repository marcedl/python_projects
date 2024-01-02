todos = []

while True:
  user_action = input("Type add, show, edit or exit: ")
  user_action = user_action.strip()
  
  match user_action:
    case 'add':
      todo = input("Enter a to do: ")
      todos.append(todo)
    case 'show': # 'show' | 'display' .... "|"" symbol means or
      for index, i in enumerate(todos): #enumerate is a function
        print(int(index) + 1, i)
    case 'edit':
      number = int(input("Number of the todo to edit: "))
      number = number - 1
      neggsew_todo = input("Enter a new to do: ")
      todos[number] = new_todo
    case 'exit':
      break
    case x: #adding an anynomous variable will match with any other input added by the user
      print("You entered a wrong command")

print("Have a nice day!")