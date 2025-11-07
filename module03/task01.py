from lib2to3.pgen2.literals import simple_escapes
size=42
length=float(input("Enter the length of zander in cm:"))
if length<size:
    calculate=size-length
    print(f"The zander is{calculate:.2f}cm short below the limit. please release it")
else:
    print("The zander is of legal size. You can keep it.")
