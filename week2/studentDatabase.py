def addStudent(database):
    name=input("enter your name: ")
    age=int(input("enter your age: "))
    math=int(input("enter maths result: "))
    phy=int(input("enter physics result: "))
    chem=int(input("enter chemistry result: "))
    average=(math+phy+chem)/3
    grade={
        "math":math,
        "phy":phy,
        "chem":chem,
        "average":average
    }
    student={
        "name":name,
        "age":age,
        "grade":grade
    }
    database[name]=student
    print("student added successfully")

def printStudent(student):
    print("|{:<10}|{:<5}|{:<5}|{:<5}|{:<5}|{:<7}|".format(student['name'],student['age'],student['grade']['math'],student['grade']['phy'],student['grade']['chem'],student['grade']['average']))
    print("____________________________________________")

def printHeader():
    print("____________________________________________")
    print("|{:<10}|{:<5}|{:<5}|{:<5}|{:<5}|{:<7}|".format("name","age","math","phy","chem","average"))
    print("____________________________________________")


def display(database):
    print("")
    printHeader()
    for student in database.values():
        printStudent(student)
    print("")


def viewStudent(database):
    name=input("enter the name of student: ")
    student=database.get(name)
    if student:
        printHeader()
        printStudent(student)
    else:
        print("student not found")

def updateStudent(database):
    update=False
    name=input("enter the name to update")
    student=database.get(name)
    if student:
        printHeader()
        printStudent(student)
        age=input("enter new age (press enter to keep current value:)")
        if age:
            student['age']=int(age)
            update=True

        math=input("enter new maths result (press enter to keep current value:)")
        if math:
            student['grade']['math']=int(math)
            update=True

        phy=input("enter new physics result (press enter to keep current value:)")
        if phy:
            student['grade']['phy']=int(phy)
            update=True
        
        chem=input("enter new chemistry result (press enter to keep current value:)")
        if chem:
            student['grade']['chem']=int(chem)
            update=True

        if update:
            average=(student['grade']['phy']+student['grade']['math']+student['grade']['chem'])
            student['grade']['average']=average
            print("student info updated successfully")
    else:
        print("the student not found in the database")

def delete(database):
    name=input("\nenter the name to delete")
    student=database.get(name)
    if student:
        database.pop(name)


def main():
    database={}

    while True:
        print("student database program")
        print("1. add student to the database.")
        print("2. search student")
        print("3. update student data")
        print("4. delete student")
        print("5. display all students")
        print("6. exit")

        choise=int(input("Enter your choise (1-6)"))

        if choise==1:
            addStudent(database)
        elif choise==2:
            viewStudent(database)
        elif choise==3:
            updateStudent(database)
        elif choise==4:
            delete(database)
        elif choise==5:
            display(database)
        elif choise==6:
            break
        else:
            print("\nwrong choise!\n")

if __name__ == '__main__':
    main()