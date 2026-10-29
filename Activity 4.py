Problem Statement
Develop a Python program to calculate an employee's salary after deductions. The program accepts the employee's name and basic salary, calculates allowances, determines deductions based on salary, and displays the gross salary, total deductions, and net salary.
2. Objectives
To understand variables and data types in Python.
To perform calculations using arithmetic operators.
To calculate allowances and gross salary.
To apply conditional statements to determine deductions.
To calculate net salary.
To display an employee's payroll details.
3. Concepts Used
Concept
Application
Variables
Store employee name and salary details
Data types
String and float
input()
Accept employee information
float()
Convert salary input into a number
Arithmetic operators
+, -, *, /
Comparison operators
<=, >, >=
Conditional statements
if, elif, else
print()
Display payroll details
4. Assumptions
For this educational example, use the following rules:
Basic salary must be greater than zero.
House Rent Allowance (HRA) is 20% of basic salary.
Dearness Allowance (DA) is 10% of basic salary.
If the basic salary is up to ₹20,000, the deduction is 5% of gross salary.
If the basic salary is above ₹20,000 and up to ₹50,000, the deduction is 10% of gross salary.
If the basic salary is above ₹50,000, the deduction is 15% of gross salary.
Gross salary = Basic salary + HRA + DA.
Net salary = Gross salary − Deduction.
Note: These percentages are assumed for this academic project and do not represent official payroll or tax rules.
5. Algorithm
Start.
Enter the employee's name.
Enter the basic salary.
Check whether the basic salary is greater than zero.
If the salary is invalid, display an error message.
Calculate HRA as 20% of basic salary.
Calculate DA as 10% of basic salary.
Calculate gross salary by adding basic salary, HRA, and DA.
If basic salary is up to ₹20,000, calculate a 5% deduction.
Otherwise, if basic salary is up to ₹50,000, calculate a 10% deduction.
Otherwise, calculate a 15% deduction.
Calculate net salary by subtracting the deduction from gross salary.
Display the employee's salary details.
Stop.
6. Flowchart
             ┌─────────────┐
             │    START    │
             └──────┬──────┘
                    │
                    ▼
        ┌────────────────────────┐
        │ Enter name and basic   │
        │ salary                 │
        └────────────┬───────────┘
                     │
                     ▼
             ┌────────────────┐
             │ Salary > 0 ?   │
             └───────┬────────┘
                 No  │  Yes
             ┌───────┘  └─────────┐
             ▼                    ▼
     ┌───────────────┐    ┌──────────────────┐
     │ Invalid Input │    │ Calculate HRA,   │
     └───────┬───────┘    │ DA and gross pay │
             │            └─────────┬────────┘
             │                      │
             │                      ▼
             │             ┌────────────────┐
             │             │ Salary <= 20000?│
             │             └───────┬────────┘
             │                 Yes │ No
             │             ┌───────┘ └──────────┐
             │             ▼                    ▼
             │      ┌─────────────┐    ┌────────────────┐
             │      │ Deduction = │    │ Salary <= 50000?│
             │      │ Gross * 5%  │    └───────┬────────┘
             │      └──────┬──────┘        Yes │ No
             │             │             ┌─────┘ └────────┐
             │             │             ▼                ▼
             │             │      ┌─────────────┐  ┌─────────────┐
             │             │      │ Deduction = │  │ Deduction = │
             │             │      │ Gross * 10% │  │ Gross * 15% │
             │             │      └──────┬──────┘  └──────┬──────┘
             │             │             │                │
             │             └─────────────┴────────────────┘
             │                           │
             │                           ▼
             │                  ┌─────────────────┐
             │                  │ Net = Gross -   │
             │                  │ Deduction       │
             │                  └────────┬────────┘
             │                           │
             │                           ▼
             │                  ┌─────────────────┐
             │                  │ Display payroll │
             │                  │ details         │
             │                  └────────┬────────┘
             │                           │
             └───────────────────────────┘
                                         ▼
                                  ┌─────────────┐
                                  │    STOP     │
                                  └─────────────┘
7. Pseudocode
START

INPUT employee_name
INPUT basic_salary

IF basic_salary <= 0 THEN
    DISPLAY "Invalid Salary"

ELSE
    HRA = basic_salary * 0.20
    DA = basic_salary * 0.10

    gross_salary = basic_salary + HRA + DA

    IF basic_salary <= 20000 THEN
        deduction = gross_salary * 0.05
    ELSE IF basic_salary <= 50000 THEN
        deduction = gross_salary * 0.10
    ELSE
        deduction = gross_salary * 0.15
    END IF

    net_salary = gross_salary - deduction

    DISPLAY employee_name
    DISPLAY basic_salary
    DISPLAY HRA
    DISPLAY DA
    DISPLAY gross_salary
    DISPLAY deduction
    DISPLAY net_salary
END IF

STOP
8. Python Source Code
Create a file named Activity_3.py.
# Employee Payroll and Deduction Analysis

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

if basic_salary <= 0:
    print("Invalid Salary")

else:
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross_salary = basic_salary + hra + da

    if basic_salary <= 20000:
        deduction = gross_salary * 0.05

    elif basic_salary <= 50000:
        deduction = gross_salary * 0.10

    else:
        deduction = gross_salary * 0.15

    net_salary = gross_salary - deduction

    print("\n--- Employee Payroll Details ---")
    print("Employee Name:", employee_name)
    print("Basic Salary: Rs.", round(basic_salary, 2))
    print("HRA: Rs.", round(hra, 2))
    print("DA: Rs.", round(da, 2))
    print("Gross Salary: Rs.", round(gross_salary, 2))
    print("Total Deduction: Rs.", round(deduction, 2))
    print("Net Salary: Rs.", round(net_salary, 2))
9. Test Cases
Test
Employee
Basic salary
Expected deduction rate
Expected net salary
1
Ravi
₹10,000
5%
₹11,400
2
Priya
₹20,000
5%
₹22,800
3
Arun
₹30,000
10%
₹29,700
4
Sita
₹50,000
10%
₹49,500
5
Kiran
₹60,000
15%
₹66,300
6
Anu
₹0
Not applicable
Invalid Salary
7
Raju
-5000
Not applicable
Invalid Salary
10. Sample Output
Test Case 1: Basic salary ₹10,000
Enter employee name: Ravi
Enter basic salary: 10000

--- Employee Payroll Details ---
Employee Name: Ravi
Basic Salary: Rs. 10000.0
HRA: Rs. 2000.0
DA: Rs. 1000.0
Gross Salary: Rs. 13000.0
Total Deduction: Rs. 650.0
Net Salary: Rs. 12350.0
Calculation check: Gross salary = ₹13,000; deduction = ₹650; net salary = ₹12,350.
Test Case 2: Basic salary ₹30,000
Enter employee name: Arun
Enter basic salary: 30000

--- Employee Payroll Details ---
Employee Name: Arun
Basic Salary: Rs. 30000.0
HRA: Rs. 6000.0
DA: Rs. 3000.0
Gross Salary: Rs. 39000.0
Total Deduction: Rs. 3900.0
Net Salary: Rs. 35100.0
Calculation check: Gross salary = ₹39,000; deduction = ₹3,900; net salary = ₹35,100.
Test Case 3: Invalid salary
Enter employee name: Anu
Enter basic salary: 0
Invalid Salary
Important correction to the test-case table
Use these correct net salary values when documenting your results:
Basic salary
Gross salary
Deduction
Correct net salary
₹10,000
₹13,000
₹650
₹12,350
₹20,000
₹26,000
₹1,300
₹24,700
₹30,000
₹39,000
₹3,900
₹35,100
₹50,000
₹65,000
₹6,500
₹58,500
₹60,000
₹78,000
₹11,700
₹66,300
11. Output Screenshots
To produce genuine screenshots for your assignment:
Open Python IDLE or VS Code.
Save the code as Activity_3.py.
Run it with basic salaries of ₹10,000, ₹30,000, and ₹60,000.
Capture the actual output for each run.
Save the screenshots with these filenames:
output_1_low_salary.png
output_2_medium_salary.png
output_3_high_salary.png
These are suggested filenames; you must capture the screenshots from your own program execution.
12. Conclusion
The Employee Payroll and Deduction Analysis program demonstrates the use of Python variables, arithmetic operators, and conditional statements to calculate gross salary, deductions, and net salary. It also checks for invalid salary inputs and displays the employee's payroll details.
