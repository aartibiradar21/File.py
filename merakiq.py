batch1_students=["shivam","Rahul","Kavya","Dhannu","Deepanshu","Nitin","Manoj","Sukrudin","Tara","Suraj","Krishna"]

student_file=open("student_list.txt","w")

for student in batch1_students:

    student_file.write(student+"\n")

student_file.close