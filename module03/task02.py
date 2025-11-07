cabin_class=input("Enter the cabin calss(Lux/A/B/C):").upper()
if cabin_class=="Lux":
         print("Upper-deck cabin with a balcony")
elif cabin_class=="A":
        print("Cabin above the car deck with window")
elif cabin_class=="B":
         print("Windowless cabin above the car deck")
elif cabin_class=="C":
        print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")