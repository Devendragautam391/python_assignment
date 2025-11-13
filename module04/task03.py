number = input("Enter a number (or press Enter to stop): ")
if number == "":
    print("No numbers were entered.")
else:
    smallest = largest = float(number)
    while True:
        number = input("Enter another number (or press Enter to stop): ")
        if number == "":
            break
        try:
            num = float(number)
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    print("Smallest number:", smallest)
    print("Largest number:", largest)

