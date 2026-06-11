num=int(input("how many student do you have"))
students_name=[]
student_marks=[]
for i in range (0,num):
    name=input("what is name of student")
    mark=int(input("how any mark student have"))
    students_name.append(name)
    student_marks.append(mark)
def average():
    aver=sum(student_marks)/len(student_marks)
    print(f"average marks is {aver}")
def minimum():
    a=min(student_marks)
    print(f"mini mark is {a}")
def maximum():
    b=max(student_marks)
    print(f"maximum mark is {b}")
dis=input("what you want to perform average/minimum/maximum/all")   
if dis=="average":
    average()
elif dis=="minimum":
     minimum()     
elif dis=="maximum":
    maximum()
elif dis == "all":
    maximum()
    average()    
    minimum()