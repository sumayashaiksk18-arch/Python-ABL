Problem Statement
Develop a Python program to calculate the total cost and profit of manufacturing products. The program considers material costs, labour charges, material wastage, machine costs, production quantity, and selling price. It then determines whether the production meets a specified profit target.
2. Objectives
Calculate the total material cost.
Calculate material wastage costs.
Calculate labour charges.
Include machine costs in production expenses.
Calculate total production cost and sales revenue.
Determine profit and profit percentage.
Check whether the required profit target is achieved.
3. Concepts Used
Variables and data types
User input and output
Arithmetic operators
Conditional statements
Basic calculations using percentages
Input validation
4. Assumptions
The material cost represents the total cost of materials before wastage.
Wastage cost is calculated as a percentage of the material cost.
Labour charges are calculated using labour hours multiplied by the hourly rate.
Machine cost is entered as a total amount.
All manufactured units are assumed to be sold.
Revenue is calculated using units produced multiplied by the selling price per unit.
Profit percentage is calculated as profit divided by total production cost, multiplied by 100.
The user enters a target profit percentage.
All monetary amounts are in Indian rupees.
These are sample calculations for an educational project.
5. Algorithm
Start.
Enter the total material cost.
Enter the material wastage percentage.
Enter the labour hours and hourly labour rate.
Enter the machine cost.
Enter the number of units produced.
Enter the selling price per unit.
Enter the target profit percentage.
Validate the inputs.
Calculate the wastage cost.
Calculate the labour cost.
Calculate the total production cost.
Calculate the total sales revenue.
Calculate the profit.
Calculate the profit percentage.
Compare the profit percentage with the target.
Display all cost details and the profitability result.
Stop.
6. Flowchart
              ┌─────────────┐
              │    START    │
              └──────┬──────┘
                     ▼
       ┌──────────────────────────┐
       │ Enter material, wastage, │
       │ labour, machine and      │
       │ selling details          │
       └────────────┬─────────────┘
                    ▼
       ┌──────────────────────────┐
       │ Are the inputs valid?    │
       └────────────┬─────────────┘
              No    │    Yes
           ┌────────┘     └────────┐
           ▼                       ▼
   ┌────────────────┐    ┌───────────────────┐
   │ Display error  │    │ Calculate wastage │
   │ message        │    │ and labour costs  │
   └───────┬────────┘    └─────────┬─────────┘
           │                       ▼
           │             ┌───────────────────┐
           │             │ Calculate total   │
           │             │ production cost   │
           │             └─────────┬─────────┘
           │                       ▼
           │             ┌───────────────────┐
           │             │ Calculate revenue │
           │             │ and profit        │
           │             └─────────┬─────────┘
           │                       ▼
           │             ┌───────────────────┐
           │             │ Calculate profit  │
           │             │ percentage        │
           │             └─────────┬─────────┘
           │                       ▼
           │             ┌───────────────────┐
           │             │ Profit percentage │
           │             │ >= target?         │
           │             └─────────┬─────────┘
           │                  Yes  │  No
           │                ┌──────┘ └────────┐
           │                ▼                 ▼
           │        ┌───────────────┐  ┌────────────────┐
           │        │ Target        │  │ Target not     │
           │        │ achieved      │  │ achieved       │
           │        └───────┬───────┘  └───────┬────────┘
           │                └────────┬─────────┘
           │                         ▼
           │               ┌──────────────────┐
           │               │ Display results  │
           │               └────────┬─────────┘
           └─────────────────────────┤
                                     ▼
                              ┌─────────────┐
                              │    STOP     │
                              └─────────────┘
7. Pseudocode
START

INPUT material_cost
INPUT wastage_percentage
INPUT labour_hours
INPUT hourly_rate
INPUT machine_cost
INPUT units_produced
INPUT selling_price
INPUT target_profit_percentage

IF any input is invalid
    DISPLAY "Invalid input"

ELSE
    wastage_cost = material_cost * wastage_percentage / 100

    labour_cost = labour_hours * hourly_rate

    total_cost = material_cost + wastage_cost
                 + labour_cost + machine_cost

    revenue = units_produced * selling_price

    profit = revenue - total_cost

    profit_percentage = profit / total_cost * 100

    DISPLAY total_cost
    DISPLAY revenue
    DISPLAY profit
    DISPLAY profit_percentage

    IF profit_percentage >= target_profit_percentage
        DISPLAY "Profit target achieved"
    ELSE
        DISPLAY "Profit target not achieved"
    END IF
END IF

STOP
8. Python Source Code
File name: Activity_8.py
# Manufacturing Cost and Profitability Analysis

material_cost = float(input("Enter material cost: "))
wastage_percentage = float(input("Enter wastage percentage: "))
labour_hours = float(input("Enter labour hours: "))
hourly_rate = float(input("Enter hourly labour rate: "))
machine_cost = float(input("Enter machine cost: "))
units_produced = int(input("Enter units produced: "))
selling_price = float(input("Enter selling price per unit: "))
target_profit = float(input("Enter target profit percentage: "))

if (material_cost <= 0 or wastage_percentage < 0
        or wastage_percentage > 100 or labour_hours < 0
        or hourly_rate < 0 or machine_cost < 0
        or units_produced <= 0 or selling_price <= 0
        or target_profit < 0):

    print("Invalid input. Please enter valid values.")

else:
    wastage_cost = material_cost * wastage_percentage / 100

    labour_cost = labour_hours * hourly_rate

    total_cost = (material_cost + wastage_cost
                  + labour_cost + machine_cost)

    revenue = units_produced * selling_price

    profit = revenue - total_cost

    profit_percentage = profit / total_cost * 100

    print("\n--- MANUFACTURING REPORT ---")
    print("Material Cost: Rs.", round(material_cost, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Labour Cost: Rs.", round(labour_cost, 2))
    print("Machine Cost: Rs.", round(machine_cost, 2))
    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Sales Revenue: Rs.", round(revenue, 2))
    print("Profit/Loss: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percentage, 2), "%")

    if profit_percentage >= target_profit:
        print("Profit Target Achieved")
    else:
        print("Profit Target Not Achieved")
9. Test Cases
Test
Total cost
Revenue
Profit
Target
Expected result
1
₹8,500
₹10,000
₹1,500
15%
Achieved
2
₹8,500
₹10,000
₹1,500
20%
Not achieved
3
₹8,500
₹8,000
-₹500
10%
Not achieved
4
Invalid
—
—
—
Invalid input
Sample calculation
Use these inputs:
Material cost = ₹5,000
Wastage percentage = 10%
Labour hours = 20
Hourly labour rate = ₹100
Machine cost = ₹1,000
Units produced = 100
Selling price per unit = ₹100
Target profit percentage = 15%
Step 1: Calculate wastage cost
Wastage cost = ₹5,000 × 10 / 100 = ₹500
Step 2: Calculate labour cost
Labour cost = 20 × ₹100 = ₹2,000
Step 3: Calculate total production cost
Total cost = ₹5,000 + ₹500 + ₹2,000 + ₹1,000 = ₹8,500
Step 4: Calculate revenue
Revenue = 100 × ₹100 = ₹10,000
Step 5: Calculate profit
Profit = ₹10,000 − ₹8,500 = ₹1,500
Step 6: Calculate profit percentage
Profit percentage = ₹1,500 / ₹8,500 × 100 = 17.65%
Since 17.65% is greater than the target of 15%, the profit target is achieved.
10. Sample Output
Enter material cost: 5000
Enter wastage percentage: 10
Enter labour hours: 20
Enter hourly labour rate: 100
Enter machine cost: 1000
Enter units produced: 100
Enter selling price per unit: 100
Enter target profit percentage: 15

--- MANUFACTURING REPORT ---
Material Cost: Rs. 5000.0
Wastage Cost: Rs. 500.0
Labour Cost: Rs. 2000.0
Machine Cost: Rs. 1000.0
Total Production Cost: Rs. 8500.0
Sales Revenue: Rs. 10000.0
Profit/Loss: Rs. 1500.0
Profit Percentage: 17.65 %
Profit Target Achieved
Output screenshots
Run the program with the sample inputs and capture the actual output.
Save the screenshots as:
output_1_profit_target_achieved.png
output_2_profit_target_not_achieved.png
output_3_loss_calculation.png
For the second screenshot, enter a target of 20%. For the third, enter a selling price of ₹80 per unit and a target of 10%.
11. Conclusion
The Manufacturing Cost and Profitability Analysis program calculates material costs, wastage, labour charges, machine costs, total production cost, revenue, and profit. It compares the calculated profit percentage with the specified target to determine whether the target has been achieved. This activity demonstrates how basic Python concepts can be applied to manufacturing cost analysis.
