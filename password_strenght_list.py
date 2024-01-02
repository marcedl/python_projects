password = input("Enter new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for p in password:
    if p.isdigit():
        digit = True

result.append(digit)

uppercase = False
for p in password:
    if p.isupper():
        uppercase = True

result.append(uppercase)

#all function: list average
#print(all(result))

if all(result) == False:
    print("Weak Password")
else:
    print("Strong Password")