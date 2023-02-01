print("------------------------")
print("Enter Student Details")
print("------------------------")
std_name=input("Name= ")
std_reg=input("Registration= ")
std_subname1=input("Subject 1 Name = ")
std_marksobt1=int(input("Subject 1 Marks= "))
std_subname2=input("Subject 2 Name = ")
std_marksobt2=int(input("Subject 2 Marks= "))
std_subname3=input("Subject 3 Name = ")
std_marksobt3=int(input("Subject 3 Marks= "))
total_marks_obt=std_marksobt1+std_marksobt2+std_marksobt3
percentage=(total_marks_obt 100)/300
print("percentage is {}".format(percentage))
