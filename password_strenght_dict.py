password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for p in password:
    if p.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for p in password:
    if p.isupper():
        uppercase = True

result["uppercase"] = uppercase

#all function: list average
#print(all(result))

print(result)

if all(result.values()) == False:
    print("Weak Password")
else:
    print("Strong Password")