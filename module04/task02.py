while True:
    inches=float(input("Enter length in inches: "))
    if inches<=0:
        print("Invalid input. Please enter a positive number.")
        break
    centimers=inches*2.54
    print(f"{inches:.2f}inches={centimers:.2f}centimeters")