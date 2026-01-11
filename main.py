import datetime
name = input("Enter your name: ")
name1 = input("Enter your age: ")
money = float(input("How much money do you earn per month?: "))
print("Hello " + name.swapcase() + ", you are " + name1 +
      " years old." + " You earn " + str(money) + " per month.")


money = int(money)
if money < 8000:
    print("You are BOMJ.")
else:
    money >= 8000
    print("You are Vladick.")


age = int(name1)
if age < 18:
    print("You are a looser - " + name.upper() + " go back to school.")
else:
    age >= 18
    print("You are big boy.")


print(name.center(50, '='))


def my_name(name):
    return name.upper()


my_name("John Pork")


def john():
    print("Hello, " + name + my_name(", John Pork") + " fucked your mom last night " +
          name1 + " times in a row.")


john()


def test():
    print("This is a test function " + name + " " +
          name1 + " loved " + my_name("John Pork"))


test()


def sum_numbers():
    a = float(input("Enter number: "))
    b = float(input("Enter another number: "))
    return a, b, a + b


a, b, total = sum_numbers()
print("The sum of " + str(a) + " and " + str(b) + " is: " + str(total))


now = datetime.datetime.now()
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("Program finished.")


def sum_name():
    a = input("Enter your name: ")
    b = str("John Pork")
    c = datetime.datetime.now()
    return a + " and " + b + " at " + c.strftime("%Y-%m-%d %H:%M:%S")


result = sum_name()
print("Friends: " + result)


def choice():
    choice = input("Are you John Pork? Choose A (yes) or B (no): ").upper()
    if choice == 'A':
        return True
    elif choice == 'B':
        return False
    else:
        return None


result = choice()
if result is True:
    print(" - You chose A (correct).")
elif result is False:
    print(" - You chose B (incorrect).")
else:
    print(" - Invalid choice.")
