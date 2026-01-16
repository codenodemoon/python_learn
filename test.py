list_of_tobaccos = {}


def keys_and_values():
    # range(1) количество повторяющихся вызовов, стоит подумать как это использовать для цикла
    for i in range(1):
        key = input("Enter name tobacco: ")
        value = input("Enter rating: ")
        list_of_tobaccos[key] = value
    return list_of_tobaccos


print("Hello! Do you want add new tobacco?"
      " Type 'Y' to add new tobacco or 'N' to exit.")
user_input = input().upper()
if user_input == 'Y':
    keys_and_values()
    print("You added new tobacco!")
    for key, value in list_of_tobaccos.items():      # итерация по ключам и значениям словаря ФИКС
        print(f"Tobacco name: {key} | RATING: {value}")
    print("Do you want add another tobacco? Type 'Y' to add new tobacco or 'N' to exit.")
    user_input = input().upper()
    if user_input == 'Y':
        keys_and_values()
        print("You added new tobacco!")
        print(f"Tobacco name: {key} | RATING: {value}")
        for key, value in list_of_tobaccos.items():      # итерация по ключам и значениям словаря ФИКС
            print(f"Tobacco name: {key} | RATING: {value}")
            print(keys_and_values())
            user_input = input().upper()
    elif user_input == 'N':
        print("Goodbye!")
    else:
        print("Invalid input. Please type 'Y' or 'N'.")
elif user_input == 'N':
    print("Goodbye!")
else:
    print("Invalid input. Please type 'Y' or 'N'.")
    user_input = input().upper()
# test git
# git new2
