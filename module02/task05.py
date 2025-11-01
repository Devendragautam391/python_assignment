talents=int(input("Enter talents:"))
pounds=int(input("Enter pounds:"))
lots=int(input("Enter lots:"))
total_grams=((talents*20*32)+(pounds*32)+lots)*13.3
kilograms=float(total_grams//1000)
grams=total_grams%1000
print("The weight in modern units:")
print(f"{kilograms} Kilograms and {grams:.2f} grams.")