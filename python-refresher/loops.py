my_variable = 'hello'

for letter in my_variable:
    print(letter)

should_continue = True

while should_continue:
    option = input("Deveria continuar (y/n)?\n")
    if option == 'n':
        should_continue = False
