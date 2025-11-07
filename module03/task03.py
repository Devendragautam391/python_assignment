g=input("Enter your gender (male/female): ").strip().lower()
h=float(input("Enter your hemoglobin level:")
if gende =="female":
    if hemoglobin < 117:
        print("Your hemoglobin level is LOW.")
    elif hemoglobin <= 155:
        print("Your hemoglobin level is NORMAL.")
    else:
        print("Your hemoglobin level is HIGH.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is LOW.")
    elif hemoglobin <= 167:
        print("Your hemoglobin level is NORMAL.")
    else:
        print("Your hemoglobin level is HIGH.")
else:
    print("Invalid input. Please enter 'male' or 'female'.")
