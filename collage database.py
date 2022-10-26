import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nirmal@2001",
    database="collge_management_data_management_system"
)
mycursor=mydb.cursor()
def insert_teacher_data():
    sql="insert into teacher_data(name,age,department) values (%s,%s,%s)"
    name=input("enter teacher name:")
    age=int(input("enter teacher age:"))
    department=input("enter teacher department:")
    val=(name,age,department)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_teacher_data():
    mycursor.execute("select * from teacher_data")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_student_data():
    sql="insert into student_data(name,age,address) values (%s,%s,%s)"
    name=input("enter your name:")
    age=int(input("enter your age:"))
    address=input("enter your address:")
    val=(name,age,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_student_data():
    mycursor.execute("select * from student_data")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_sports_winner():
    sql="insert into sports_winner(name,department,sports) values (%s,%s,%s)"
    name=input("enter student name:")
    department=(input("enter student department:"))
    sports=input("enter your sports:")
    val=(name,department,sports)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_sports_winner():
    mycursor.execute("select * from sports_winner")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_fees_due_student():
    sql="insert into fees_due_student(name,department,due_amount) values (%s,%s,%s)"
    name=input("enter student name:")
    department=(input("enter student department:"))
    due_amount=int("enter student due_amount:")
    val=(name,department,due_amount)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_fees_due_student():
    mycursor.execute("select * from fees_due_student")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_department_wise_goodmarks():
    sql="insert into department_wise_goodmarks(name,department,total_marks) values (%s,%s,%s)"
    name=input("enter student name:")
    department=(input("enter student department:"))
    total_marks=int("enter student total_marks:")
    val=(name,department,total_marks)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_department_wise_goodmarks():
    mycursor.execute("select * from department_wise_goodmarks")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_university_exam_preparation():
    sql="insert into university_exam_preparation(date,subject,total_marks) values (%s,%s,%s)"
    date=int(input("enter exam date:"))
    subject=(input("enter department subject:"))
    total_marks=int(input("enter student total_marks:"))
    val=(date,subject,total_marks)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_university_exam_preparation():
    mycursor.execute("select * from university_exam_preparation ")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_student_transport_information():
    sql="insert into student_transport_information(student,department,transport) values (%s,%s,%s)"
    student=input("enter name of student:")
    department=(input("enter department :"))
    transport=input("enter transport:")
    val=(student,department,transport)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_student_transport_information():
    mycursor.execute("select * student_transport_information ")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_lab_using_department():
    sql="insert into lab_using_department(department,total_student) values (%s,%s,%s)"
    department=input("enter exam date:")
    total_student=int(input("enter department subject:"))
    val=(department,total_student)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_lab_using_department():
    mycursor.execute("select * lab_using_department ")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
def insert_passed_out_students_data():
   sql="insert passed_out_students_data (name,passed_out_year) value(%s,%s)"
   name=input("enter your name:")
   passed_out_year=int(input("enter passed out year:"))
   val=(name,passed_out_year)
   mycursor.execute(sql,val)
   mydb.commit()
   print("data entered successfully")
def view_passed_out_students_data():
   mycursor.execute("SELECT * FROM passed_out_students_data;")
   result=mycursor.fetchall()
   for i in result:
       print(i)
def insert_student_parents_information():
    sql="insert into student_parents_information(stud_name,department,parent_name,parent_phone_number) values (%s,%s,%s,%s)"
    stud_name=input("enter studentname:")
    department=input("enter student department:")
    parent_name=input("enter student parent name:")
    parent_phone_number=int(input("enter parent phone number:"))
    val=(stud_name,department,parent_name,parent_phone_number)
    mycursor.execute(sql,val)
    mydb.commit()
    print("added sucessfully")
def veiw_student_parents_information():
    mycursor.execute("select * student_parents_information ")
    result=mycursor.fetchall()
    for i in result:
        print(i) 
print("1->teacher_data") 
print("2->view_teacher_data")
print("3->insert_student_data")
print("4->view_student_data")
print("5->insert_sport_winner")
print("6->view_sport_winner")
print("7->insert_fees_due_student")
print("8->view_fees_due_student")
print("9->insert_department_wise_goodmarks")
print("10->view_department_wise_goodmarks")
print("11->insert_university_exam_preparation")
print("12->view_university_exam_preparation")
print("13->insert_student_transport_information") 
print("14->view_student_transport_information")
print("15->insert_lab_using_department")
print("16->view_lab_using_department")
print("17->insert_passed_out_students_data") 
print("18->view_passed_out_students_data")
print("19->insert_student_parents_information")
print("20->view_student_parents_information")
try:
   user=int(input("enter the number:"))
   if user==1:
    insert_teacher_data()
   elif user==2:
    veiw_teacher_data()
   elif user==3:
    insert_student_data()
   elif user==4:
    veiw_student_data()
   elif user==5:
    insert_sports_winner()
   elif user==6:
    veiw_sports_winner()
   elif user==7:
    insert_fees_due_student()
   elif user==8:
    veiw_fees_due_student()
   elif user==9:
    insert_department_wise_goodmarks()
   elif user==10:
    veiw_department_wise_goodmarks()
   elif user==11:
    insert_university_exam_preparation()
   elif user==12:
    veiw_university_exam_preparation()
   elif user==13:
    insert_student_transport_information()
   elif user==14:
    veiw_student_transport_information()
   elif user==15:
    insert_lab_using_department()
   elif user==16:
    veiw_lab_using_department()
   elif user==17:
    insert_passed_out_students_data()
   elif user==18:
    view_passed_out_students_data()
   elif user==19:
    insert_student_parents_information()
   elif user==20:
    veiw_student_parents_information()
   else:
    print("data not found")
except:
    print("enter numbers only")