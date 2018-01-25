# should_continue = True
# if should_continue:
#     print("hello")
#
# known_people = ["John", "Ana", "Mary"]
# person = input("Enter the name of the person you know:\n")
#
# if person in known_people:
#     print("Você conhece alguem")
# else:
#     print("Você conhece ngm")

## Exercise


def who_do_you_know():
    # Ask the user for a list of people you know
    # Split the string into a list
    # Return that list
    people = input("Digite o nome das pessoas que você conhece separado por espaços (apenas primeiro nome):\n").split(
        " "
    )
    people = [p.strip().lower() for p in people]
    return people


def ask_user():
    # Ask user for a name
    # See if their name is in the list of people they know
    # Print out that they know the person
    people_you_know = who_do_you_know()
    person = input("Digite o nome da pessoa:\n")
    if person in people_you_know:
        print("You know {}".format(person))
    else:
        print("Unfortunately, you dont know {}".format(person))


ask_user()
