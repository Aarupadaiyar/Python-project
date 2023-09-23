s1=int(input('What is the score of the student a in subject1? '))
s2=int(input('What is the score of the student a in subject2? '))
s3=int(input('What is the score of the student a in subject3? '))
s4=int(input('What is the score of the student a in subject4? '))
s5=int(input('What is the score of the student a in subject5? '))
s6=int(input('What is the score of the student a in subject5? '))
a=print(f"The total mark of the student is {s1+s2+s3+s4+s5+s6} out of 600")
x=(((s1+s2+s3+s4+s5+s6)/600)*100)
print(f"The overall percentage of the student is {x}%")
if x>=90:
    print("you secured First class mark with flying colors of A grade . Keep it up :)")
elif 90>x>=80:
    print("you secured Second Class mark with good grade of B . You are so much capable to do better so try hard to get first grade marks :)")
elif 80>x>=70:
    print("you secured Third class mark with C grade , this is satisfactory for your immense effort but you need more smart work to score good :|")
elif 70>x>=60:
    print("You secured fourth class mark with D grade which is not enough , so try hard and rock your next exam")
else:
    print("You are least scorer which means you didn't clear your concept , it is not that much issues teacher are there to just clear your doubts , so please clear your concept and work hard with teachers support and your final grades are E")

