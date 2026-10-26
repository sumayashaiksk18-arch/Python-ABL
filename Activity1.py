1. Problem Statement
A university wants to allocate scholarships to students based on their marks and annual family income. Write a Python program that accepts a student's name, marks, and annual family income, then checks the eligibility criteria and displays the scholarship category.
2. Objectives
- To understand and use variables in Python.
- To accept input from the user.
- To use data types such as strings, integers, and floating-point numbers.
- To perform comparisons using relational operators.
- To apply if-elif-else conditional statements.
- To determine scholarship eligibility based on marks and family income.
3. Concepts Used
Concept	Usage in this program
Variables	Store student name, marks, and family income
String	Store the student's name
Float	Store marks and annual family income
input()	Accept student details
float()	Convert numeric input into a number
Comparison operators	>=, <=, <, >
Logical operator	and
Conditional statements	if, elif, else
print()	Display the result


4. Assumptions
For this example, the university follows these assumed rules:
- Students must score at least 80 marks to qualify for a scholarship.
- Students with annual family income up to ₹2,50,000 receive a 100% scholarship.
- Students with annual family income up to ₹5,00,000 receive a 50% scholarship.
- Students who do not meet these conditions are not eligible.
- Marks must be between 0 and 100.
- Annual family income cannot be negative.
Note: These are example eligibility rules for this program, not official university scholarship rules.
5. Algorithm
1. Start.
2. Enter the student's name.
3. Enter the student's marks.
4. Enter the annual family income.
5. Check whether marks are between 0 and 100 and income is non-negative.
6. If the input is invalid, display an error message.
7. Otherwise, check whether marks are at least 80.
8. If marks are below 80, display “Not Eligible.”
9. If marks are at least 80 and income is at most ₹2,50,000, display “100% Scholarship.”
10. Otherwise, if income is at most ₹5,00,000, display “50% Scholarship.”
11. Otherwise, display “Not Eligible.”
12. Stop.
6. Flowchart
          ┌─────────────┐
          │    START    │
          └──────┬──────┘
                 │
                 ▼
       ┌─────────────────────┐
       │ Enter name, marks,  │
       │ and annual income   │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Marks between 0-100 │
       │ and income >= 0?    │
       └──────────┬──────────┘
             No   │   Yes
          ┌───────┘   └────────┐
          ▼                    ▼
  ┌────────────────┐   ┌────────────────┐
  │ Display Invalid│   │ Marks >= 80?   │
  │ Input          │   └───────┬────────┘
  └───────┬────────┘       No  │  Yes
          │             ┌──────┘  └────────┐
          │             ▼                  ▼
          │       ┌─────────────┐  ┌─────────────────┐
          │       │ Not Eligible│  │ Income <= 250000?│
          │       └──────┬──────┘  └────────┬────────┘
          │              │             Yes  │  No
          │              │          ┌───────┘ └────────┐
          │              │          ▼                  ▼
          │              │   ┌──────────────┐  ┌────────────────┐
          │              │   │ 100%         │  │ Income <=      │
          │              │   │ Scholarship  │  │ 500000?        │
          │              │   └──────┬───────┘  └───────┬────────┘
          │              │          │             Yes  │  No
          │              │          │          ┌───────┘ └───────┐
          │              │          │          ▼                 ▼
          │              │          │   ┌──────────────┐  ┌─────────────┐
          │              │          │   │ 50%          │  │ Not Eligible│
          │              │          │   │ Scholarship  │  └──────┬──────┘
          │              │          │   └──────┬───────┘         │
          └──────────────┴──────────┴──────────┴─────────────────┘
                                      │
                                      ▼
                               ┌─────────────┐
                               │     STOP    │
                               └─────────────┘

7. Pseudocode
START

INPUT student_name
INPUT marks
INPUT annual_income

IF marks < 0 OR marks > 100 OR annual_income < 0 THEN
    DISPLAY "Invalid Input"

ELSE IF marks < 80 THEN
    DISPLAY "Not Eligible"

ELSE IF annual_income <= 250000 THEN
    DISPLAY "100% Scholarship"

ELSE IF annual_income <= 500000 THEN
    DISPLAY "50% Scholarship"

ELSE
    DISPLAY "Not Eligible"

END IF

STOP

8. Python Source Code
Create a file named Activity_1.py.                                                                                                                                      
# University Scholarship Allocation

student_name = input("Enter student name: ")
marks = float(input("Enter marks out of 100: "))
annual_income = float(input("Enter annual family income in rupees: "))

print("\n--- Scholarship Details ---")
print("Student Name:", student_name)
print("Marks:", marks)
print("Annual Family Income:", annual_income)

if marks < 0 or marks > 100 or annual_income < 0:
    print("Invalid Input")

elif marks < 80:
    print("Scholarship Status: Not Eligible")

elif annual_income <= 250000:
    print("Scholarship Status: 100% Scholarship")

elif annual_income <= 500000:
    print("Scholarship Status: 50% Scholarship")

else:
    print("Scholarship Status: Not Eligible")
| Test | Student name | Marks | Annual income | Expected result |
|---|---|---:|---:|---|
| 1 | Ravi | 90 | ₹2,00,000 | 100% Scholarship |
| 2 | Priya | 85 | ₹4,00,000 | 50% Scholarship |
| 3 | Arun | 70 | ₹2,00,000 | Not Eligible |
| 4 | Sita | 90 | ₹6,00,000 | Not Eligible |
| 5 | Kiran | 105 | ₹2,00,000 | Invalid Input |
| 6 | Anu | 85 | -1000 | Invalid Input |
10. Sample Output
Example 1 — 100% Scholarship
Enter student name: Ravi
Enter marks out of 100: 90
Enter annual family income in rupees: 200000

--- Scholarship Details ---
Student Name: Ravi
Marks: 90.0
Annual Family Income: 200000.0
Scholarship Status: 100% Scholarship

Example 2 — 50% Scholarship
Enter student name: Priya
Enter marks out of 100: 85
Enter annual family income in rupees: 400000

--- Scholarship Details ---
Student Name: Priya
Marks: 85.0
Annual Family Income: 400000.0
Scholarship Status: 50% Scholarship

Example 3 — Not Eligible
Enter student name: Arun
Enter marks out of 100: 70
Enter annual family income in rupees: 200000

--- Scholarship Details ---
Student Name: Arun
Marks: 70.0
Annual Family Income: 200000.0
Scholarship Status: Not Eligible

Output screenshots
To obtain genuine screenshots for your submission:
1. Open Python IDLE, VS Code, or another Python editor.
2. Enter and save the code as Activity_1.py.
3. Run the program using the test cases above.
4. Take screenshots showing the code and the actual output.
5. Save them inside the activity folder.
Suggested screenshot names:
- output_1_100_percent.png
- output_2_50_percent.png
- output_3_not_eligible.png
These are suggested filenames; the screenshots still need to be captured after running the program.
11. Conclusion
The University Scholarship Allocation program demonstrates how Python variables, data types, input/output statements, comparison operators, logical operators, and conditional statements can be used to solve a real-world problem. The program evaluates students' marks and annual family income to determine scholarship eligibility.
