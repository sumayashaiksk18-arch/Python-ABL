1. Problem Statement
Develop a Python program to calculate an electricity bill based on the number of units consumed by a household. The program should apply progressive billing rates according to the units consumed and display the total electricity bill.
2. Objectives
- To understand variables and data types in Python.
- To accept electricity units from the user.
- To use arithmetic operators for calculating the bill.
- To use comparison operators for checking unit ranges.
- To apply conditional statements to determine the applicable billing rate.
- To display the final electricity bill.
3. Concepts Used
Concept	Application
Variables	Store consumer name, units, and bill amount
Data types	String, integer, and float
input()	Accept user details
int()	Convert units into an integer
Arithmetic operators	+, -, *
Comparison operators	<, <=, >, >=
Conditional statements	if, elif, else
print()	Display bill details


4. Assumptions
For this example, the following electricity rates are assumed:
- First 100 units: ₹2 per unit.
- Next 100 units (101–200): ₹3 per unit.
- Units above 200: ₹5 per unit.
- A consumer who uses 0 units will have a bill of ₹0.
- Negative units are invalid.
- The bill is calculated progressively, meaning each rate applies only to the units in that slab.
Note: These are sample rates for an educational program, not official electricity tariff rates.
5. Algorithm
1. Start.
2. Enter the consumer's name.
3. Enter the number of electricity units consumed.
4. Check whether the units are negative.
5. If units are negative, display an invalid input message.
6. If units are between 0 and 100, calculate the bill at ₹2 per unit.
7. If units are between 101 and 200, calculate ₹200 for the first 100 units and ₹3 per additional unit.
8. If units exceed 200, calculate ₹200 for the first 100 units, ₹300 for the next 100 units, and ₹5 per additional unit.
9. Display the consumer's name, units consumed, and total bill.
10. Stop.
6. Flowchart
             ┌─────────────┐
             │    START    │
             └──────┬──────┘
                    │
                    ▼
        ┌────────────────────────┐
        │ Enter name and units   │
        └────────────┬───────────┘
                     │
                     ▼
            ┌────────────────┐
            │ Units < 0 ?    │
            └───────┬────────┘
                Yes │ No
             ┌──────┘ └─────────┐
             ▼                  ▼
     ┌───────────────┐    ┌────────────────┐
     │ Invalid Input │    │ Units <= 100 ? │
     └───────┬───────┘    └───────┬────────┘
             │                Yes │ No
             │             ┌──────┘ └────────┐
             │             ▼                 ▼
             │     ┌──────────────┐   ┌────────────────┐
             │     │ Bill = Units │   │ Units <= 200 ? │
             │     │      * 2     │   └───────┬────────┘
             │     └──────┬───────┘       Yes │ No
             │            │             ┌─────┘ └────────┐
             │            │             ▼                ▼
             │            │     ┌────────────────┐ ┌─────────────────┐
             │            │     │ Bill = 200 +   │ │ Bill = 500 +    │
             │            │     │ (Units-100)*3  │ │ (Units-200)*5   │
             │            │     └───────┬────────┘ └────────┬────────┘
             │            │             │                   │
             └────────────┴─────────────┴───────────────────┘
                                          │
                                          ▼
                              ┌────────────────────────┐
                              │ Display electricity   │
                              │ bill                  │
                              └───────────┬────────────┘
                                          │
                                          ▼
                                   ┌─────────────┐
                                   │    STOP     │
                                   └─────────────┘

7. Pseudocode
START

INPUT consumer_name
INPUT units

IF units < 0 THEN
    DISPLAY "Invalid Input"

ELSE IF units <= 100 THEN
    bill = units * 2

ELSE IF units <= 200 THEN
    bill = 200 + (units - 100) * 3

ELSE
    bill = 500 + (units - 200) * 5

END IF

IF units >= 0 THEN
    DISPLAY consumer_name
    DISPLAY units
    DISPLAY bill
END IF

STOP

8. Python Source Code
Create a Python file named Activity_2.py.
# Progressive Electricity Billing

consumer_name = input("Enter consumer name: ")
units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid Input: Units cannot be negative")

elif units <= 100:
    bill = units * 2
    print("Consumer Name:", consumer_name)
    print("Units Consumed:", units)
    print("Electricity Bill: Rs.", bill)

elif units <= 200:
    bill = 200 + (units - 100) * 3
    print("Consumer Name:", consumer_name)
    print("Units Consumed:", units)
    print("Electricity Bill: Rs.", bill)

else:
    bill = 500 + (units - 200) * 5
    print("Consumer Name:", consumer_name)
    print("Units Consumed:", units)
    print("Electricity Bill: Rs.", bill)
How the calculation works
For 250 units:
- First 100 units: 100 × ₹2 = ₹200
- Next 100 units: 100 × ₹3 = ₹300
- Remaining 50 units: 50 × ₹5 = ₹250
Total bill = ₹750
9. Test Cases
Test case	Consumer	Units	Expected output
1	Ravi	50	₹100
2	Priya	100	₹200
3	Arun	150	₹350
4	Sita	200	₹500
5	Kiran	250	₹750
6	Anu	0	₹0
7	Raju	-10	Invalid input


10. Sample Output
Test Case 1: 50 units
Enter consumer name: Ravi
Enter electricity units consumed: 50
Consumer Name: Ravi
Units Consumed: 50
Electricity Bill: Rs. 100

Test Case 2: 150 units
Enter consumer name: Priya
Enter electricity units consumed: 150
Consumer Name: Priya
Units Consumed: 150
Electricity Bill: Rs. 350

Test Case 3: 250 units
Enter consumer name: Kiran
Enter electricity units consumed: 250
Consumer Name: Kiran
Units Consumed: 250
Electricity Bill: Rs. 750

Output screenshots
To create the actual screenshots required by your assignment:
1. Open Python IDLE or VS Code.
2. Type or paste the code into Activity_2.py.
3. Run the program.
4. Test it with 50, 150, and 250 units.
5. Capture screenshots showing the program output.
Save the screenshots with these names:
- output_1_50_units.png
- output_2_150_units.png
- output_3_250_units.png
These are suggested filenames; capture the screenshots from your actual program execution.
11. Conclusion
The Progressive Electricity Billing program demonstrates the use of Python variables, data types, arithmetic operators, comparison operators, and conditional statements. It calculates an electricity bill based on progressive unit rates and handles invalid negative inputs.
Upload to your GitHub Python-ABL repository
Use this folder structure:
Python-ABL/
│
├── README.md
│
└── Activity_2_Progressive_Electricity_Billing/
    ├── Activity_2.py
    ├── Problem_Statement.txt
    ├── Objectives.txt
    ├── Assumptions.txt
    ├── Algorithm.txt
    ├── Flowchart.txt
    ├── Pseudocode.txt
    ├── Test_Cases.txt
    ├── Conclusion.txt
    └── Screenshots/
        ├── output_1_50_units.png
        ├── output_2_150_units.png
        └── output_3_250_units.png
