name=input("enter student name:")
print("student:",name)
english=int(input("enter english marks:"))
python=int(input("enter python marks"))
maths=int(input("enter maths marks"))
science=int(input("enter science marks"))
computer=int(input("enter computer marks"))
total=english+python+maths+science+computer
print("total marks:",total)
percentage=total/500*100
print("percentage:",percentage,"%")
if percentage>=79:
    print=("A")
elif percentage>=70:
    print=("B")
elif percentage>=60:
    print("C")
elif percentage>=50:
    print("D")

else:
    print("fail")
    print("grade:",grade)
