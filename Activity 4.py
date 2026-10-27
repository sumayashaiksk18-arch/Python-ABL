1. Problem Statement
Develop a Python program to calculate a patient's hospital bill based on the number of days admitted, daily room charges, and medical charges. The program should calculate the total bill and classify the patient based on the total amount.
2. Objectives
To understand variables and data types in Python.
To perform calculations using arithmetic operators.
To calculate hospital room charges and medical charges.
To use conditional statements for patient classification.
To display the total hospital bill and patient category.
3. Concepts Used
Concept
Application
Variables
Store patient details and charges
Data types
String, integer, and float
input()
Accept patient information
int()
Convert hospital stay into days
float()
Convert charges into numbers
Arithmetic operators
+, *
Comparison operators
<, <=, >
Conditional statements
if, elif, else
print()
Display the bill
4. Assumptions
For this educational project, assume the following charges:
Daily room charge: ₹2,000.
Medical charges are entered by the user.
Total bill = Room charges + Medical charges.
If the total bill is below ₹10,000, classify the patient as Category A — Low Bill.
If the total bill is ₹10,000 to ₹30,000, classify the patient as Category B — Medium Bill.
If the total bill exceeds ₹30,000, classify the patient as Category C — High Bill.
The number of hospital days must be greater than zero.
Medical charges cannot be negative.
Note: These are sample billing and classification rules for an academic exercise, not actual hospital rates or medical classifications.
5. Algorithm
Start.
Enter the patient's name.
Enter the number of hospital days.
Enter the medical charges.
Check whether the number of days is greater than zero and medical charges are non-negative.
If the input is invalid, display an error message.
Calculate room charges by multiplying hospital days by ₹2,000.
Calculate the total bill by adding room charges and medical charges.
If the total bill is below ₹10,000, classify the patient as Category A.
Otherwise, if the total bill is at most ₹30,000, classify the patient as Category B.
Otherwise, classify the patient as Category C.
Display the patient details, total bill, and category.
Stop.
6. Flowchart
             ┌─────────────┐
             │    START    │
             └──────┬──────┘
                    │
                    ▼
        ┌────────────────────────┐
        │ Enter patient name,    │
        │ days and medical fees  │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │ Days > 0 and medical   │
        │ charges >= 0?          │
        └────────────┬───────────┘
               No   │   Yes
          ┌─────────┘   └─────────┐
          ▼                       ▼
  ┌─────────────────┐    ┌───────────────────┐
  │ Display Invalid │    │ Room charges =     │
  │ Input           │    │ Days × 2000        │
  └────────┬────────┘    └─────────┬─────────┘
           │                       ▼
           │             ┌───────────────────┐
           │             │ Total = Room      │
           │             │ + Medical charges │
           │             └─────────┬─────────┘
           │                       ▼
           │             ┌───────────────────┐
           │             │ Total < 10000?    │
           │             └─────────┬─────────┘
           │                   Yes │ No
           │              ┌────────┘ └────────┐
           │              ▼                   ▼
           │       ┌──────────────┐   ┌────────────────┐
           │       │ Category A  │   │ Total <= 30000?│
           │       └──────┬───────┘   └───────┬────────┘
           │              │               Yes │ No
           │              │          ┌────────┘ └────────┐
           │              │          ▼                   ▼
           │              │   ┌──────────────┐    ┌──────────────┐
           │              │   │ Category B   │    │ Category C   │
           │              │   └──────┬───────┘    └──────┬───────┘
           │              │          │                   │
           │              └──────────┴───────────────────┘
           │                         │
           │                         ▼
           │                ┌──────────────────┐
           │                │ Display bill and │
           │                │ patient category │
           │                └────────┬─────────┘
           │                         │
           └─────────────────────────┘
                                     ▼
                              ┌─────────────┐
                              │    STOP     │
                              └─────────────┘
7. Pseudocode
START

INPUT patient_name
INPUT hospital_days
INPUT medical_charges

IF hospital_days <= 0 OR medical_charges < 0 THEN
    DISPLAY "Invalid Input"

ELSE
    room_charges = hospital_days * 2000
    total_bill = room_charges + medical_charges

    IF total_bill < 10000 THEN
        category = "Category A - Low Bill"

    ELSE IF total_bill <= 30000 THEN
        category = "Category B - Medium Bill"

    ELSE
        category = "Category C - High Bill"
    END IF

    DISPLAY patient_name
    DISPLAY room_charges
    DISPLAY medical_charges
    DISPLAY total_bill
    DISPLAY category
END IF

STOP
8. Python Source Code
Create a file named Activity_4.py.
# Hospital Billing and Patient Classification

patient_name = input("Enter patient name: ")
hospital_days = int(input("Enter number of hospital days: "))
medical_charges = float(input("Enter medical charges: "))

if hospital_days <= 0 or medical_charges < 0:
    print("Invalid Input")

else:
    room_charges = hospital_days * 2000
    total_bill = room_charges + medical_charges

    if total_bill < 10000:
        category = "Category A - Low Bill"

    elif total_bill <= 30000:
        category = "Category B - Medium Bill"

    else:
        category = "Category C - High Bill"

    print("\n--- Hospital Bill Details ---")
    print("Patient Name:", patient_name)
    print("Hospital Days:", hospital_days)
    print("Room Charges: Rs.", room_charges)
    print("Medical Charges: Rs.", medical_charges)
    print("Total Bill: Rs.", total_bill)
    print("Patient Category:", category)
9. Test Cases
Test
Patient
Days
Medical charges
Expected total bill
Expected category
1
Ravi
2
₹2,000
₹6,000
Category A
2
Priya
5
₹5,000
₹15,000
Category B
3
Arun
10
₹15,000
₹35,000
Category C
4
Sita
1
₹8,000
₹10,000
Category B
5
Kiran
0
₹1,000
Invalid input
—
6
Anu
2
-500
Invalid input
—
10. Sample Output
Test Case 1: Category A
Enter patient name: Ravi
Enter number of hospital days: 2
Enter medical charges: 2000

--- Hospital Bill Details ---
Patient Name: Ravi
Hospital Days: 2
Room Charges: Rs. 4000
Medical Charges: Rs. 2000.0
Total Bill: Rs. 6000.0
Patient Category: Category A - Low Bill
Test Case 2: Category B
Enter patient name: Priya
Enter number of hospital days: 5
Enter medical charges: 5000

--- Hospital Bill Details ---
Patient Name: Priya
Hospital Days: 5
Room Charges: Rs. 10000
Medical Charges: Rs. 5000.0
Total Bill: Rs. 15000.0
Patient Category: Category B - Medium Bill
Test Case 3: Category C
Enter patient name: Arun
Enter number of hospital days: 10
Enter medical charges: 15000

--- Hospital Bill Details ---
Patient Name: Arun
Hospital Days: 10
Room Charges: Rs. 20000
Medical Charges: Rs. 15000.0
Total Bill: Rs. 35000.0
Patient Category: Category C - High Bill
Output screenshots
To create the actual screenshots required for your assignment:
Open Python IDLE or VS Code.
Save the program as Activity_4.py.
Run the program with the inputs from Test Cases 1, 2, and 3.
Capture screenshots showing the actual output.
Save them using these suggested filenames:
output_1_category_A.png
output_2_category_B.png
output_3_category_C.png
These are filenames only; you must capture the screenshots after running the program.
11. Conclusion
The Hospital Billing and Patient Classification program demonstrates the use of Python variables, arithmetic operators, and conditional statements. It calculates hospital room charges and medical expenses, determines the total bill, and assigns a billing category based on the total amount.
