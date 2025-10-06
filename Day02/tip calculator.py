print("Welcome to the tip calculator!")
total=input("how much is the total bill?")
tip=input("how much is the tip 10,20 or 25?")
mem=float(input("how many members are in your party?"))
amound=(int(total) * int(tip) / 100 + int(total)) / mem
final_amound=(round(amound,2))
print(f"each induviduals should pay {final_amound}")

