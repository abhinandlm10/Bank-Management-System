
#Program of STUDENT SCHOOL REPORTS
import mysql.connector

#connecting python with sql database
connector=mysql.connector.connect(host="localhost",user="root",password="Sreeganga@123",database="school")

#connecting python with sql database
cursor=connector.cursor()

#executing the sql quary
cursor.execute("create table if not exists student (student_name varchar(30),admission_no int,fathers_name varchar(30),mothers_name varchar(30),phone_number int,address varchar(50),student_section varchar(30))")
connector.commit()
cursor.execute("create table if not exists marks (admission_no int,english int,computer_science int,physics int,chemistry int,maths int)")
connector.commit()


#Function defenition for adding student details
def add_student():
    student_name=input("enter the student name:")
    admission_no=int(input("enter the admission number of the student:"))
    fathers_name=input("enter the fathers name of the student:")
    mothers_name=input("enter the mothers name of the student:")
    phone_number=int(input("enter the phone number:"))
    address=input("enter the address of the student:")
    student_section=input("enter the student section:")
    cursor.execute("insert into student (student_name,admission_no,fathers_name,mothers_name,phone_number,address,student_section) values ('{}','{}','{}','{}','{}','{}','{}')".format(student_name,admission_no,fathers_name,mothers_name,phone_number,address,student_section))
    connector.commit()
    print("Student Details Added Successfully.......")


#Function defenition for viewing student details
def view_student():
    admission_no=int(input("enter the admission number:"))
    if admission_no is not None:
        cursor.execute("select * from student where admission_no='{}'".format(admission_no))
        admission=cursor.fetchone()[1]
        if admission==admission_no:
            cursor.execute("select * from student where admission_no='{}'".format(admission_no))
            student_name,admission_no,fathers_name,mothers_name,phone_number,address,student_section=cursor.fetchone()
            print("name of student:",student_name)
            print("admission number of student:",admission_no)
            print("fathers name of student:",fathers_name)
            print("mothers name of student:",mothers_name)
            print("phone number of student:",phone_number)
            print("address of student:",address)
            print("section of student:",student_section)
        else:
            print("There is no such student in the School!")


#Function defenition for adding marks of student
def add_mark():
    admission_no=int(input("enter the admission number of the student:"))
    english=float(input("enter the marks of english:"))
    computer_science=float(input("enter the marks of computer science:"))
    physics=float(input("enter the marks of physics:"))
    chemistry=float(input("enter the marks of chemistry:"))
    maths=float(input("enter the marks of maths:"))
    cursor.execute("insert into marks (admission_no,english,computer_science,physics,chemistry,maths) values ('{}','{}','{}','{}','{}','{}')".format(admission_no,english,computer_science,physics,chemistry,maths))
    connector.commit()
    print("Marks updated Succesfully.......")


#Function defenition for updating student details
def update_student():
    admission_no=int(input("enter the admission number:"))
    cursor.execute("select * from student where admission_no='{}'".format(admission_no))
    admission=cursor.fetchone()[1]
    if admission==admission_no:
        sname=input("enter the student name:")
        fname=input("enter the fathers name of the student:")
        mname=input("enter the mothers name of the student:")
        pnumber=int(input("enter the phone number:"))
        addr=input("enter the address of the student:")
        ssection=input("enter the student section:")
        cursor.execute("update student set student_name='{}',fathers_name='{}',mothers_name='{}',phone_number='{}',address='{}',student_section='{}' where admission_no='{}'".format(sname,fname,mname,pnumber,addr,ssection,admission_no))
        connector.commit()
        s=cursor.fetchone()
        print("Student Details Updated Succesfully.......")
    else:
        print(f"Such student with admission number {admission_no} not Found!")


#Function defenition for viewing student details including the mark report of the student
def generate_student():
    admission_no=int(input("enter the admission number:"))
    cursor.execute("select st.admission_no,st.student_name,st.fathers_name,st.mothers_name,st.phone_number,st.address,st.student_section,mr.english,mr.computer_science,mr.physics,mr.chemistry,mr.maths from student st,marks mr where st.admission_no=mr.admission_no and st.admission_no='{}'".format(admission_no))
    admission,student_name,fathers_name,mothers_name,phone_number,address,student_section,english,computer_science,physics,chemistry,maths=cursor.fetchone()
    if admission==admission_no:
        print("Admission number:",admission_no)
        print("name of student:",student_name)
        print("admission number of student:",admission_no)
        print("fathers name of student:",fathers_name)
        print("mothers name of student:",mothers_name)
        print("phone number of student:",phone_number)
        print("address of student:",address)
        print("section of student:",student_section)
        print("Marks of English:",english)
        print("Marks of Conputer Science:",computer_science)
        print("Marks of Physics:",physics)
        print("Marks of Chemistry:",chemistry)
        print("Marks of Maths:",maths)
    else:
        print(f"Such student with admission number {admission_no} not Found!")
        
 


#presenting the opening page 
while True:
    print("========VIMALA CENTRAL SCHOOL=========")
    print("1.add student details")
    print("2.view student details")
    print("3.update student details")
    print("4.add student mark details")
    print("5.generate student wise report")
    print("6.exit")

    choice=input("enter the choice(1-6):")

    #entering the users choice 
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        update_student()
    elif choice=="4":
        add_mark()   
    elif choice=="5":
        generate_student()
    elif choice=="6":
        break
    else:
        print("Invalid Choice,Try Again!")

cursor.close()

