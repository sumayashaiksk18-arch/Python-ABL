Problem Statement
Develop a Python program to generate a retail bill for multiple products. The program should calculate product costs based on quantity, apply category-specific taxes, provide discounts when the purchase reaches a specified amount, enforce a maximum discount limit, and display the final invoice.
2. Objectives
Calculate the total cost of multiple products.
Apply different tax rates to different product categories.
Apply discounts when the purchase meets a minimum threshold.
Ensure that the discount does not exceed the maximum allowed amount.
Display an itemized bill and the final payable amount.
Practise Python variables, operators, conditional statements, and loops.
3. Assumptions
The following rules are used for this educational example:
Product category
Tax rate
Food
5%
Clothing
12%
Electronics
18%
Additional rules:
The program processes three products per bill.
Each product has a name, category, unit price, and quantity.
The subtotal is the sum of the price multiplied by the quantity for each product.
Tax is calculated separately for each product category.
A 10% discount is applied when the subtotal is at least ₹2,000.
The maximum discount is ₹500.
Tax is calculated on the original subtotal before the discount.
The final bill is calculated as subtotal + tax − discount.
Product prices must be positive, and quantities must be greater than zero.
These are sample rules, not the rules of a specific retailer.
4. Algorithm
Start.
Set the subtotal and total tax to zero.
Repeat the following steps for three products:
Enter the product name.
Enter its category.
Enter the unit price.
Enter the quantity.
Validate the price and quantity.
Calculate the product amount.
Determine the category-specific tax rate.
Calculate the tax for the product.
Add the amount and tax to their respective totals.
Check whether the subtotal is at least ₹2,000.
If eligible, calculate a 10% discount.
If the discount exceeds ₹500, limit it to ₹500.
Otherwise, set the discount to zero.
Calculate the final bill.
Display the subtotal, tax, discount, and final amount.
Stop.
5. Flowchart
             ┌─────────────┐
             │    START    │
             └──────┬──────┘
                    ▼
        ┌──────────────────────┐
        │ Subtotal = 0          │
        │ Total tax = 0         │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Enter product details│
        │ for 3 products       │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Validate price and   │
        │ quantity             │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Calculate product    │
        │ amount and category  │
        │ tax                  │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Update subtotal and  │
        │ total tax            │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Subtotal >= ₹2000?   │
        └──────────┬───────────┘
              Yes  │  No
           ┌───────┘ └─────────┐
           ▼                   ▼
   ┌────────────────┐  ┌────────────────┐
   │ Calculate 10%  │  │ Discount = 0   │
   │ discount       │  │                │
   └───────┬────────┘  └───────┬────────┘
           ▼                   │
   ┌────────────────┐          │
   │ Discount > ₹500?│         │
   └───────┬────────┘          │
           ▼                   │
   ┌────────────────┐          │
   │ Limit discount │          │
   │ to ₹500 if     │          │
   │ necessary      │          │
   └───────┬────────┘          │
           └─────────┬─────────┘
                     ▼
        ┌──────────────────────┐
        │ Calculate final bill │
        │ Subtotal + Tax       │
        │ - Discount           │
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐
        │ Display invoice      │
        └──────────┬───────────┘
                   ▼
             ┌─────────────┐
             │    STOP     │
             └─────────────┘
6. Pseudocode
START

subtotal = 0
total_tax = 0

REPEAT 3 TIMES
    INPUT product_name
    INPUT category
    INPUT price
    INPUT quantity

    IF price <= 0 OR quantity <= 0
        DISPLAY "Invalid product details"
        STOP
    END IF

    amount = price * quantity

    IF category = "Food"
        tax_rate = 5
    ELSE IF category = "Clothing"
        tax_rate = 12
    ELSE IF category = "Electronics"
        tax_rate = 18
    ELSE
        DISPLAY "Invalid category"
        STOP
    END IF

    tax = amount * tax_rate / 100

    subtotal = subtotal + amount
    total_tax = total_tax + tax
END REPEAT

IF subtotal >= 2000
    discount = subtotal * 10 / 100

    IF discount > 500
        discount = 500
    END IF
ELSE
    discount = 0
END IF

final_bill = subtotal + total_tax - discount

DISPLAY subtotal
DISPLAY total_tax
DISPLAY discount
DISPLAY final_bill

STOP
7. Python Source Code
File name: Activity_7.py
# Retail Billing with Multiple Discount Rules

subtotal = 0
total_tax = 0

for i in range(3):
    print("\nEnter details for product", i + 1)

    name = input("Product name: ")
    category = input("Category (Food/Clothing/Electronics): ")
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))

    if price <= 0 or quantity <= 0:
        print("Invalid product details")
        break

    if category == "Food":
        tax_rate = 5

    elif category == "Clothing":
        tax_rate = 12

    elif category == "Electronics":
        tax_rate = 18

    else:
        print("Invalid category")
        break

    amount = price * quantity
    tax = amount * tax_rate / 100

    subtotal = subtotal + amount
    total_tax = total_tax + tax

else:
    if subtotal >= 2000:
        discount = subtotal * 10 / 100

        if discount > 500:
            discount = 500

    else:
        discount = 0

    final_bill = subtotal + total_tax - discount

    print("\n----- RETAIL INVOICE -----")
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Total Tax: Rs.", round(total_tax, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
Note: The for...else structure in this beginner program displays the invoice only if all three product entries finish without executing break. If any product details or category are invalid, the program stops processing the invoice.
8. Test Cases
Test
Subtotal
Total tax
Discount
Final bill
1. Discount applies
₹2,500
₹390
₹250
₹2,640
2. Below threshold
₹500
₹25
₹0
₹525
3. Maximum discount applies
₹6,000
₹900
₹500
₹6,400
4. Invalid price
—
—
—
Error message
5. Invalid category
—
—
—
Error message
Sample calculation: Test 1
Clothing: ₹1,000 × 1 = ₹1,000; tax = ₹120.
Electronics: ₹1,500 × 1 = ₹1,500; tax = ₹270.
Subtotal = ₹1,000 + ₹1,500 = ₹2,500.
Total tax = ₹120 + ₹270 = ₹390.
Discount = 10% of ₹2,500 = ₹250.
Final bill = ₹2,500 + ₹390 − ₹250 = ₹2,640.
Sample calculation: Test 3
Subtotal = ₹6,000.
Total tax = ₹900.
Calculated discount = 10% of ₹6,000 = ₹600.
Maximum permitted discount = ₹500.
Final bill = ₹6,000 + ₹900 − ₹500 = ₹6,400.
9. Sample Output
Enter details for product 1
Product name: Shirt
Category (Food/Clothing/Electronics): Clothing
Unit price: 1000
Quantity: 1

Enter details for product 2
Product name: Headphones
Category (Food/Clothing/Electronics): Electronics
Unit price: 1500
Quantity: 1

Enter details for product 3
Product name: Bread
Category (Food/Clothing/Electronics): Food
Unit price: 0
Quantity: 1
Invalid product details
The example above demonstrates input validation. To produce the successful invoice for Test 1, enter a valid third product, such as Bread priced at ₹50 with quantity 1. The resulting bill will include that additional product and its tax, so the final values will differ from Test 1.
Output Screenshot Instructions
Save the code as Activity_7.py.
Run it in Python IDLE or VS Code.
Enter valid details for all three products.
Capture a screenshot of the completed invoice.
Test the maximum-discount rule and capture another screenshot.
Save the screenshots as:
output_1_retail_invoice.png
output_2_maximum_discount.png
Capture these screenshots from the actual program; the sample output is only an example.
10. Conclusion
The Retail Billing program demonstrates how Python can calculate product costs, apply category-specific taxes, and provide conditional discounts. It also enforces a maximum discount limit and displays the final bill. This activity helps develop an understanding of variables, loops, arithmetic operators, and conditional statements.
