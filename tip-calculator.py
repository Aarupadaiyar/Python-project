print("Welcome to the tip calculator.")
bill=input("What was the total bill? $")
per=input("What percentage tip would you like to give? 10,12 or 15? ")
bills=int(bill)
pers=int(per)
people=input("How many people to split the bill? ")
peoples=int(people)
x=bills*(pers/100)
y=bills+x
z=y/peoples
print(f"Each person should pay: ${z}")
