#a py program to determine the eligibility to vote
name=(input("enter your official name: "))
age=int(input("enter your age: "))
citizenship=(input("enter citizenship: ")).lower
if(age>=18 and citizenship == "kenyan"):
    print(name)
    print(age)
    print("eligible to vote")
else:
    print(name)
    print(age)
    print("not eligible to vote")