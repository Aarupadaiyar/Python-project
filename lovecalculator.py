print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combine=name1+name2
lowercase=combine.lower()
t=lowercase.count("t")
r=lowercase.count("r")
u=lowercase.count("u")
e=lowercase.count("e")
true=t+r+u+e
l=lowercase.count("l")
o=lowercase.count("o")
v=lowercase.count("v")
e=lowercase.count("e")
love=l+o+v+e
trueloves=str(true)+str(love)
truelove=int(trueloves)
if (truelove < 10) or (truelove > 90):
    print(f"Love score for {name1} and {name2}  is {truelove}, you go together like coke and mentos.")
elif (truelove >= 40) and (truelove <= 50):
    print(f"Love score for {name1} and {name2} is {truelove}, you are alright together.")
else:
    print(f"Love score for {name1} and {name2} is {truelove}, and you make up a good loved ones with working for your relationship lil.")