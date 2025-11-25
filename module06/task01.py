month = int(input("Enter a month number (1–12): "))
seasons = ("Winter", "Spring", "Summer", "Autumn")
if 1 <= month <= 12:
    season_index = ((month % 12) // 3)
    print(seasons[season_index])
else:
    print("Invalid month number.")
