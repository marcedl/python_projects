todos = []

while True:
  user_action = input("Type add, show or exit: ")
  user_action = user_action.strip()
  
  match user_action:
    case 'add':
      todo = input("Enter a to do: ")
      todos.append(todo)
    case 'show': # 'show' | 'display' .... "|"" symbol means or
      for i in todos:
        i = i.title()
        print(i)
    case 'exit':
      break
    case x: #adding an anynomous variable will match with any other input added by the user
      print("You entered a wrong command")

print("Have a nice day!")