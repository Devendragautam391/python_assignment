numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
numbers.sort(reverse=True)
print("The five greatest numbers are:")
for n in numbers[:5]:
    print(n)
