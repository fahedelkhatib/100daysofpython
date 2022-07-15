# Day 2 - Tip Calculator

print("Welcome to the tip calculator.")

totalbill = float(input("What was the total bill? $"))
percenttip = input("What percentage tip would you like to give? 10, 12, or 15? ")
peoplesplit = int(input("How many people will split the bill? "))

tip = float("1." + percenttip)
personprice = round((totalbill / peoplesplit) * tip, 2)
print(f"Each person should pay: ${personprice}")