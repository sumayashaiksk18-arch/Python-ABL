Problem Statement
Develop a Python program to compare different mobile recharge plans based on usage, validity, and budget. The program calculates the total cost of each plan, including extra usage charges, checks which plans satisfy the user's requirements, and identifies the most economical eligible plan.
2. Objectives
To understand variables and data types in Python.
To perform calculations using arithmetic operators.
To compare mobile plans using comparison operators.
To apply conditional statements to select an eligible plan.
To calculate additional charges for exceeding plan limits.
To identify the most economical plan within the given budget.
3. Concepts Used
Concept
Application
Variables
Store usage, budget, and plan costs
Data types
Strings, integers, and floats
input()
Accept user requirements
Arithmetic operators
+, -, *
Comparison operators
<, <=, >
Logical operators
and, or
Conditional statements
if, elif, else
print()
Display plan details
4. Assumptions
The following sample mobile plans are used for this project:
Plan
Base price
Included minutes
Validity
Extra charge
Basic
₹199
200 minutes
30 days
₹1 per extra minute
Standard
₹299
400 minutes
30 days
₹1 per extra minute
Premium
₹399
600 minutes
30 days
₹1 per extra minute
Additional assumptions:
The user enters the expected usage in minutes.
The user enters the required validity in days.
The user enters the maximum available budget.
All three plans have a validity of 30 days.
Extra charges apply only when usage exceeds the included minutes.
A plan is eligible when its validity meets the requirement and its total cost is within the budget.
The eligible plan with the lowest total cost is selected.
Negative usage, non-positive validity, and negative budgets are invalid inputs.
These are fictional sample plans and rates for an academic project, not actual telecom offers.
5. Algorithm
Start.
Enter expected usage in minutes.
Enter required validity in days.
Enter the available budget.
Check whether the inputs are valid.
Calculate the Basic plan cost, including extra usage charges if applicable.
Calculate the Standard plan cost, including extra usage charges if applicable.
Calculate the Premium plan cost, including extra usage charges if applicable.
Initialize the selected plan as "No eligible plan."
Check whether the Basic plan satisfies the validity and budget requirements.
If eligible, select it as the current best plan.
Check the Standard plan and replace the current selection if it is eligible and cheaper.
Check the Premium plan and replace the current selection if it is eligible and cheaper.
Display the cost of each plan and the most economical eligible plan.
If no plan satisfies the requirements, display an appropriate message.
Stop.
6. Flowchart
             ┌─────────────┐
             │    START    │
             └──────┬──────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │ Enter usage, validity,  │
       │ and budget              │
       └────────────┬────────────┘
                    │
                    ▼
       ┌─────────────────────────┐
       │ Are all inputs valid?   │
       └────────────┬────────────┘
               No   │   Yes
          ┌─────────┘   └──────────┐
          ▼                        ▼
  ┌─────────────────┐    ┌─────────────────────┐
  │ Display Invalid │    │ Calculate Basic,    │
  │ Input           │    │ Standard, Premium   │
  └────────┬────────┘    │ plan costs          │
           │             └──────────┬──────────┘
           │                        │
           │                        ▼
           │             ┌─────────────────────┐
           │             │ Initialize selected │
           │             │ plan                │
           │             └──────────┬──────────┘
           │                        │
           │                        ▼
           │             ┌─────────────────────┐
           │             │ Basic eligible?     │
           │             └──────────┬──────────┘
           │                        │
           │                        ▼
           │             ┌─────────────────────┐
           │             │ Check Standard plan │
           │             │ and select if it is │
           │             │ cheaper and eligible│
           │             └──────────┬──────────┘
           │                        │
           │                        ▼
           │             ┌─────────────────────┐
           │             │ Check Premium plan  │
           │             │ and select if it is │
           │             │ cheaper and eligible│
           │             └──────────┬──────────┘
           │                        │
           │                        ▼
           │             ┌─────────────────────┐
           │             │ Display selected    │
           │             │ plan and total cost │
           │             └──────────┬──────────┘
           │                        │
           └────────────────────────┘
                                    ▼
                             ┌─────────────┐
                             │    STOP     │
                             └─────────────┘
7. Pseudocode
START

INPUT usage_minutes
INPUT required_days
INPUT budget

IF usage_minutes < 0 OR required_days <= 0 OR budget < 0 THEN
    DISPLAY "Invalid Input"

ELSE
    CALCULATE Basic plan cost
    CALCULATE Standard plan cost
    CALCULATE Premium plan cost

    selected_plan = "No eligible plan"
    lowest_cost = 0

    IF required_days <= 30 AND Basic cost <= budget THEN
        selected_plan = "Basic"
        lowest_cost = Basic cost
    END IF

    IF required_days <= 30 AND Standard cost <= budget THEN
        IF selected_plan = "No eligible plan" OR Standard cost < lowest_cost THEN
            selected_plan = "Standard"
            lowest_cost = Standard cost
        END IF
    END IF

    IF required_days <= 30 AND Premium cost <= budget THEN
        IF selected_plan = "No eligible plan" OR Premium cost < lowest_cost THEN
            selected_plan = "Premium"
            lowest_cost = Premium cost
        END IF
    END IF

    DISPLAY all plan costs
    DISPLAY selected_plan

    IF selected_plan = "No eligible plan" THEN
        DISPLAY "No plan meets your requirements"
    ELSE
        DISPLAY lowest_cost
    END IF
END IF

STOP
8. Python Source Code
File name: Activity_5.py
# Multi-Plan Telecommunications Cost Optimization

usage = int(input("Enter expected usage in minutes: "))
required_days = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget in rupees: "))

if usage < 0 or required_days <= 0 or budget < 0:
    print("Invalid Input")

else:
    # Basic Plan
    basic_cost = 199

    if usage > 200:
        basic_cost = basic_cost + (usage - 200) * 1

    # Standard Plan
    standard_cost = 299

    if usage > 400:
        standard_cost = standard_cost + (usage - 400) * 1

    # Premium Plan
    premium_cost = 399

    if usage > 600:
        premium_cost = premium_cost + (usage - 600) * 1

    selected_plan = "No eligible plan"
    lowest_cost = 0

    # Check Basic Plan
    if required_days <= 30 and basic_cost <= budget:
        selected_plan = "Basic"
        lowest_cost = basic_cost

    # Check Standard Plan
    if required_days <= 30 and standard_cost <= budget:
        if selected_plan == "No eligible plan" or standard_cost < lowest_cost:
            selected_plan = "Standard"
            lowest_cost = standard_cost

    # Check Premium Plan
    if required_days <= 30 and premium_cost <= budget:
        if selected_plan == "No eligible plan" or premium_cost < lowest_cost:
            selected_plan = "Premium"
            lowest_cost = premium_cost

    print("\n--- Mobile Plan Comparison ---")
    print("Basic Plan Cost: Rs.", basic_cost)
    print("Standard Plan Cost: Rs.", standard_cost)
    print("Premium Plan Cost: Rs.", premium_cost)

    print("Selected Plan:", selected_plan)

    if selected_plan == "No eligible plan":
        print("No plan meets your requirements")
    else:
        print("Total Cost: Rs.", lowest_cost)
9. Test Cases
Test
Usage
Required validity
Budget
Expected result
1
150 minutes
28 days
₹250
Basic — ₹199
2
350 minutes
28 days
₹400
Standard — ₹299
3
550 minutes
30 days
₹500
Premium — ₹399
4
100 minutes
35 days
₹500
No eligible plan
5
700 minutes
30 days
₹450
No eligible plan
6
-10 minutes
30 days
₹500
Invalid input
7
100 minutes
30 days
-100
Invalid input
10. Sample Outputs
Test Case 1: Basic Plan
Enter expected usage in minutes: 150
Enter required validity in days: 28
Enter your budget in rupees: 250

--- Mobile Plan Comparison ---
Basic Plan Cost: Rs. 199
Standard Plan Cost: Rs. 299
Premium Plan Cost: Rs. 399
Selected Plan: Basic
Total Cost: Rs. 199
Test Case 2: Standard Plan
Enter expected usage in minutes: 350
Enter required validity in days: 28
Enter your budget in rupees: 400

--- Mobile Plan Comparison ---
Basic Plan Cost: Rs. 349
Standard Plan Cost: Rs. 299
Premium Plan Cost: Rs. 399
Selected Plan: Standard
Total Cost: Rs. 299
Test Case 3: Premium Plan
Enter expected usage in minutes: 550
Enter required validity in days: 30
Enter your budget in rupees: 500

--- Mobile Plan Comparison ---
Basic Plan Cost: Rs. 549
Standard Plan Cost: Rs. 449
Premium Plan Cost: Rs. 399
Selected Plan: Premium
Total Cost: Rs. 399
Output Screenshots
Run the Python program and capture genuine screenshots of the output for Test Cases 1, 2, and 3.
Suggested filenames:
output_1_basic_plan.png
output_2_standard_plan.png
output_3_premium_plan.png
These are suggested filenames; capture the screenshots from your actual program execution.
11. Conclusion
The Multi-Plan Telecommunications Cost Optimization program demonstrates the use of Python variables, arithmetic operators, comparison operators, logical operators, and conditional statements. It calculates the total cost of different mobile plans, considers validity and budget requirements, and identifies the most economical eligible plan.
