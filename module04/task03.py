numbers=[]
while True:
    user_input=input("Enter a number (or press Enter to stop): ")
    if user_input=="":
        break
    number = float(user_input)
    numbers.append(number)
if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"\nSmallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("\nNo numbers were entered.")
