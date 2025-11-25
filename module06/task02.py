names = set()
while True:
    name = input("Enter a name (or press Enter to quit): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("\nFinal Output:")
for n in names:
    print(n)
