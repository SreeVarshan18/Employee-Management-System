import sqlite3 as s
from prettytable import PrettyTable

connection = s.connect("Employees_Management_System.db")

listoftables = connection.execute("SELECT name from sqlite_master WHERE type='table' AND name='EMPLOYEES'").fetchall()

if listoftables != []:
    print("Table already exist")
else:
    connection.execute(''' CREATE TABLE EMPLOYEES(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    EMP_CODE INTEGER,
                    NAME TEXT,
                    PHONE INTEGER,
                    EMAIL TEXT,
                    DESIGNATION TEXT,
                    SALARY INTEGER,
                    COMPANY_NAME TEXT
    ) ''')
    print("Table created Successfully")

while True:
    print("Select an option from the MENU")
    print("1.Add the Employees ")
    print("2.View all Employees ")
    print("3.Search an Employee using Employee Name")
    print("4.Update an employee details using employee Code ")
    print("5.Delete an employee using employee Code ")
    print("6.Display all the details of employees whose salary is greater than 50000 ")
    print("7.Display the count of total number of employees in the company ")
    print("8.Display all the employee details in alphabetical order, within the specific salary range")
    print("9.Display all the employees data, whose salary is less than the average salary of all the employees ")
    print("10.Exit ")

    choice = int(input("Enter a Choice: "))

    if choice == 1:
        a = input("Enter Employee Code: ")
        b = input("Enter Employee Name: ")
        c = input("Enter Phone Number: ")
        d = input("Enter Email: ")
        e = input("Enter Designation: ")
        f = input("Enter Salary: ")
        g = input("Enter Company Name: ")

        connection.execute(" INSERT INTO EMPLOYEES(EMP_CODE, NAME, PHONE, EMAIL, \
        DESIGNATION, SALARY, COMPANY_NAME) VALUES(" + a + ",'" + b + "'," + c + ",'" + d + "',\
        '" + e + "'," + f + ",'" + g + "')")
        connection.commit()
        print("Inserted Successfully")


    elif choice == 2:
        result = connection.execute("SELECT * FROM EMPLOYEES")
        table = PrettyTable(["ID", "Employee Code", "Employee Name", "Phone Number", "Email", "Designation",
                             "Salary", "Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)


    elif choice == 3:
        name = input("Enter Employee Name: ")

        result = connection.execute("SELECT * FROM EMPLOYEES WHERE NAME='" + name + "'")
        table = PrettyTable(["ID", "Employee Code", "Employee Name", "Phone Number", "Email", "Designation",
                             "Salary", "Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)


    elif choice == 4:
        code = input("Enter Employee Code: ")

        getNempcode = input("Enter New Employee Code: ")
        getNname = input("Enter New Employee Name: ")
        getNphone = input("Enter New Phone Number: ")
        getNemail = input("Enter New Email: ")
        getNdesig = input("Enter New Designation: ")
        getNsalary = input("Enter New Salary: ")
        getNcompanyname = input("Enter New Company Name: ")

        result = connection.execute(" UPDATE EMPLOYEES SET EMP_CODE=" + getNempcode + ", NAME='" + getNname + "', \
                PHONE=" + getNphone + ", EMAIL='" + getNemail + "', DESIGNATION='" + getNdesig + "',\
                SALARY=" + getNsalary + ", COMPANY_NAME='" + getNcompanyname + "' WHERE EMP_CODE=" + code)
        connection.commit()
        print("Updated Successfully")

    elif choice == 5:
        code = input("Enter Employee Code: ")

        result = connection.execute("DELETE FROM EMPLOYEES WHERE EMP_CODE=" + code)
        connection.commit()
        print("Deleted Successfully")
    elif choice == 6:

        result = connection.execute("SELECT * FROM EMPLOYEES WHERE SALARY>50000")
        table = PrettyTable(["ID", "Employee Code", "Employee Name", "Phone Number", "Email", "Designation",
                             "Salary", "Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)


    elif choice == 7:

        result = connection.execute("SELECT COUNT(*) as count FROM EMPLOYEES ")
        table = PrettyTable(
            ["Count"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 8:
        Low = input("Enter low Salary: ")
        High = input("Enter High Salary: ")

        result = connection.execute(
            "SELECT * FROM EMPLOYEES WHERE SALARY BETWEEN " + Low + " AND " + High + " ORDER BY NAME ASC")
        table = PrettyTable(["ID", "Employee Code", "Employee Name", "Phone Number", "Email", "Designation",
                             "Salary", "Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)

    elif choice == 9:
        result = connection.execute(
            "SELECT * FROM EMPLOYEES WHERE SALARY<(SELECT AVG(SALARY) as sal FROM EMPLOYEES )")
        table = PrettyTable(["ID", "Employee Code", "Employee Name", "Phone Number", "Email", "Designation",
                             "Salary", "Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)


    elif choice == 10:
        connection.close()
        break

    else:
        print("Invalid Option")

