Problem Statement
Develop a Python program to analyse travel expenses in different currencies. The program converts expenses into Indian rupees using supplied exchange rates, adds currency conversion fees, compares total spending against a travel budget, and identifies the largest expense category.
2. Objectives
Accept travel expenses in different currencies.
Convert expenses into Indian rupees.
Calculate currency conversion fees.
Calculate the total travel expenditure.
Compare expenses against a given budget.
Identify the largest expense category.
Practise Python variables, arithmetic operators, and conditional statements.
3. Concepts Used
Variables and data types
User input and output
Arithmetic operators
Conditional statements
String handling
Comparison operators
Basic calculations using percentages
4. Assumptions
The program considers three expense categories: airfare, accommodation, and food.
Each expense can be entered in a different currency.
The user supplies the exchange rate in Indian rupees per unit of foreign currency.
A conversion fee of 2% is applied to each converted expense.
The conversion fee is included in the total travel expenditure.
The total expenditure is compared with the user's budget.
The program identifies the category with the highest total expense, including its conversion fee.
The exchange rates used in the sample output are hypothetical and are not live exchange rates.
5. Algorithm
Start.
Enter the travel budget in Indian rupees.
Enter the airfare amount and its exchange rate.
Enter the accommodation amount and its exchange rate.
Enter the food expense and its exchange rate.
Validate the inputs.
Convert each expense into Indian rupees.
Calculate the 2% conversion fee for each expense.
Add the conversion fee to each converted expense.
Calculate the total travel expenditure.
Compare the total expenditure with the budget.
Identify the largest expense category.
Display the converted expenses, fees, total expenditure, budget status, and largest expense category.
Stop.
6. Flowchart
              ┌─────────────┐
              │    START    │
              └──────┬──────┘
                     ▼
        ┌────────────────────────┐
        │ Enter travel budget,   │
        │ expense amounts and    │
        │ exchange rates         │
        └────────────┬───────────┘
                     ▼
        ┌────────────────────────┐
        │ Are inputs valid?      │
        └────────────┬───────────┘
                No   │   Yes
             ┌───────┘   └────────┐
             ▼                    ▼
      ┌──────────────┐    ┌──────────────────┐
      │ Display      │    │ Convert expenses │
      │ error        │    │ into INR         │
      └──────┬───────┘    └────────┬─────────┘
             │                     ▼
             │            ┌──────────────────┐
             │            │ Calculate 2%     │
             │            │ conversion fees  │
             │            └────────┬─────────┘
             │                     ▼
             │            ┌──────────────────┐
             │            │ Calculate total  │
             │            │ travel expenses  │
             │            └────────┬─────────┘
             │                     ▼
             │            ┌──────────────────┐
             │            │ Compare total    │
             │            │ with budget      │
             │            └────────┬─────────┘
             │                     ▼
             │            ┌──────────────────┐
             │            │ Find largest     │
             │            │ expense category │
             │            └────────┬─────────┘
             │                     ▼
             │            ┌──────────────────┐
             │            │ Display results  │
             │            └────────┬─────────┘
             │                     │
             └─────────────────────┤
                                   ▼
                            ┌─────────────┐
                            │    STOP     │
                            └─────────────┘
7. Pseudocode
START

INPUT budget

INPUT airfare_amount
INPUT airfare_rate

INPUT hotel_amount
INPUT hotel_rate

INPUT food_amount
INPUT food_rate

IF any amount or exchange rate is negative
    DISPLAY "Invalid input"

ELSE
    airfare = airfare_amount * airfare_rate
    hotel = hotel_amount * hotel_rate
    food = food_amount * food_rate

    airfare_fee = airfare * 2 / 100
    hotel_fee = hotel * 2 / 100
    food_fee = food * 2 / 100

    airfare_total = airfare + airfare_fee
    hotel_total = hotel + hotel_fee
    food_total = food + food_fee

    total_expenses = airfare_total + hotel_total + food_total

    IF total_expenses <= budget
        DISPLAY "Within budget"
    ELSE
        DISPLAY "Budget exceeded"
    END IF

    IF airfare_total >= hotel_total AND
       airfare_total >= food_total
        DISPLAY "Airfare is the largest expense"
    ELSE IF hotel_total >= food_total
        DISPLAY "Accommodation is the largest expense"
    ELSE
        DISPLAY "Food is the largest expense"
    END IF

    DISPLAY all expenses and fees
    DISPLAY total_expenses
END IF

STOP
8. Python Source Code
File name: Activity_9.py
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in INR: "))

print("\nEnter Airfare Details")
airfare_amount = float(input("Enter airfare in foreign currency: "))
airfare_rate = float(input("Enter exchange rate to INR: "))

print("\nEnter Accommodation Details")
hotel_amount = float(input("Enter accommodation cost in foreign currency: "))
hotel_rate = float(input("Enter exchange rate to INR: "))

print("\nEnter Food Expense Details")
food_amount = float(input("Enter food cost in foreign currency: "))
food_rate = float(input("Enter exchange rate to INR: "))

if (budget < 0 or airfare_amount < 0 or airfare_rate <= 0
        or hotel_amount < 0 or hotel_rate <= 0
        or food_amount < 0 or food_rate <= 0):

    print("Invalid input. Please enter valid values.")

else:
    airfare = airfare_amount * airfare_rate
    hotel = hotel_amount * hotel_rate
    food = food_amount * food_rate

    airfare_fee = airfare * 2 / 100
    hotel_fee = hotel * 2 / 100
    food_fee = food * 2 / 100

    airfare_total = airfare + airfare_fee
    hotel_total = hotel + hotel_fee
    food_total = food + food_fee

    total_expenses = airfare_total + hotel_total + food_total

    print("\n--- TRAVEL BUDGET REPORT ---")
    print("Airfare with fee: Rs.", round(airfare_total, 2))
    print("Accommodation with fee: Rs.", round(hotel_total, 2))
    print("Food with fee: Rs.", round(food_total, 2))
    print("Total Expenses: Rs.", round(total_expenses, 2))
    print("Travel Budget: Rs.", round(budget, 2))

    if total_expenses <= budget:
        print("Status: Within Budget")
    else:
        print("Status: Budget Exceeded")

    if airfare_total >= hotel_total and airfare_total >= food_total:
        print("Largest Expense: Airfare")

    elif hotel_total >= food_total:
        print("Largest Expense: Accommodation")

    else:
        print("Largest Expense: Food")
9. Test Cases
Test
Budget
Airfare total
Accommodation total
Food total
Expected result
1
₹60,000
₹25,398
₹18,360
₹16,065
Within budget
2
₹50,000
₹25,398
₹18,360
₹16,065
Budget exceeded
3
₹30,000
₹10,200
₹15,300
₹5,100
Within budget
4
₹20,000
₹25,398
₹18,360
₹16,065
Budget exceeded
5
Any
Negative expense
—
—
Invalid input
Sample calculation
Use the following sample inputs:
Travel budget: ₹60,000
Airfare: 300 foreign currency units
Airfare exchange rate: ₹83 per unit
Accommodation: 200 foreign currency units
Accommodation exchange rate: ₹90 per unit
Food: 150 foreign currency units
Food exchange rate: ₹105 per unit
Airfare
Converted airfare = 300 × ₹83 = ₹24,900
Conversion fee = ₹24,900 × 2% = ₹498
Airfare total = ₹24,900 + ₹498 = ₹25,398
Accommodation
Converted accommodation cost = 200 × ₹90 = ₹18,000
Conversion fee = ₹18,000 × 2% = ₹360
Accommodation total = ₹18,000 + ₹360 = ₹18,360
Food
Converted food cost = 150 × ₹105 = ₹15,750
Conversion fee = ₹15,750 × 2% = ₹315
Food total = ₹15,750 + ₹315 = ₹16,065
Total travel expenditure
₹25,398 + ₹18,360 + ₹16,065 = ₹59,823
Budget remaining = ₹60,000 − ₹59,823 = ₹177
Airfare is the largest expense category, and the total expenditure is within budget.
10. Sample Output
Enter travel budget in INR: 60000

Enter Airfare Details
Enter airfare in foreign currency: 300
Enter exchange rate to INR: 83

Enter Accommodation Details
Enter accommodation cost in foreign currency: 200
Enter exchange rate to INR: 90

Enter Food Expense Details
Enter food cost in foreign currency: 150
Enter exchange rate to INR: 105

--- TRAVEL BUDGET REPORT ---
Airfare with fee: Rs. 25398.0
Accommodation with fee: Rs. 18360.0
Food with fee: Rs. 16065.0
Total Expenses: Rs. 59823.0
Travel Budget: Rs. 60000.0
Status: Within Budget
Largest Expense: Airfare
Output screenshots
Run the program and capture actual screenshots for these scenarios:
Within budget: Use a budget of ₹60,000.
Budget exceeded: Use a budget of ₹50,000.
Different largest expense: Use inputs that make accommodation the largest expense.
Save them with these filenames:
output_1_within_budget.png
output_2_budget_exceeded.png
output_3_largest_expense.png
These filenames are suggestions. Capture the screenshots from your own program execution.
11. Conclusion
The Multi-Currency Travel Budget Analysis program converts travel expenses into Indian rupees using supplied exchange rates. It calculates conversion fees, determines total expenditure, compares spending against a budget, and identifies the largest expense category. This activity demonstrates how Python variables, arithmetic operators, and conditional statements can be used for travel budget planning.
