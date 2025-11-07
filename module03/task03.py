g=input("Enter your gender (male/female): ").strip().lower()
h=float(input("Enter your hemoglobin level:"))
if g=="female":
    if h<117:
        print("Your hemoglobin level is LOW.")
    elif h<=155:
        print("Your hemoglobin level is NORMAL.")
    else:
        print("Your hemoglobin level is HIGH.")
elif g=="male":
    if h<134:
        print("Your hemoglobin level is LOW.")
    elif h<=167:
        print("Your hemoglobin level is NORMAL.")
    else:
        print("Your hemoglobin level is HIGH.")
else:
    print("Invalid input. Please enter 'male' or 'female'.")
