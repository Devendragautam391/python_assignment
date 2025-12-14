airports = {}
while True:
    choice = input("1 add, 2 fetch, 3 quit: ")
    if choice == "1":
        icao = input("Icao Code:")
        name = input("Airport Name:")
        airports[icao] = name
        print("Airport saved!")
    elif choice == "2":
        icao = input("Icao Code:")
        print(airports.get(icao, "Airport not found."))
    elif choice == "3":
        print("Goodbye!")
        break


