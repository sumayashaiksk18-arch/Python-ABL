Problem Statement
A college is organizing a campus event. Calculate the total event expenses, participant registration income, sponsorship income, and final profit or loss. Also determine the minimum number of participants required to break even.
2. Objectives
Calculate fixed and participant-based expenses.
Calculate total event expenditure.
Calculate registration and sponsorship income.
Determine the event's profit or loss.
Find the minimum participants needed to break even.
3. Assumptions
All amounts are entered in Indian Rupees (₹).
Venue and equipment are fixed costs.
Catering, transport, and certificates are charged per participant.
Each participant pays the same registration fee.
Sponsorship is a fixed amount.
These are sample values for learning purposes.
4. Algorithm
Start.
Input venue and equipment costs.
Input catering, transport, and certificate costs per participant.
Input the number of participants, registration fee, and sponsorship.
Calculate fixed costs and cost per participant.
Calculate total event cost.
Calculate total income from registrations and sponsorship.
Calculate profit or loss.
Calculate the minimum participants needed to break even, if possible.
Display the results.
Stop.
5. Flowchart
       START
         |
    Input all costs,
    participants, fee
    and sponsorship
         |
   Calculate fixed cost
   and cost per person
         |
   Calculate total cost
    and total income
         |
   Calculate profit/loss
         |
   Is sponsorship >=
      fixed cost?
      /       \
    Yes        No
     |          |
 Minimum = 0  Is registration
              fee > cost per
              participant?
              /       \
            Yes        No
             |          |
       Calculate     Break-even
       minimum       not possible
       participants  with current fee
              \       /
               Display
               results
                  |
                 STOP

6. Pseudocode
START

INPUT venue_cost
INPUT equipment_cost
INPUT catering_per_person
INPUT transport_per_person
INPUT certificate_per_person
INPUT participants
INPUT registration_fee
INPUT sponsorship

fixed_cost = venue_cost + equipment_cost

cost_per_person = catering_per_person
                  + transport_per_person
                  + certificate_per_person

total_cost = fixed_cost + (cost_per_person * participants)

registration_income = registration_fee * participants

total_income = registration_income + sponsorship

profit_or_loss = total_income - total_cost

IF fixed_cost <= sponsorship
    minimum_participants = 0
ELSE IF registration_fee > cost_per_person
    contribution = registration_fee - cost_per_person
    remaining_cost = fixed_cost - sponsorship
    minimum_participants =
        (remaining_cost + contribution - 1) // contribution
ELSE
    Break-even is not possible with the current fee
END IF

DISPLAY total_cost
DISPLAY total_income
DISPLAY profit_or_loss

STOP

7. Python Source Code
Filename: Activity_10.py
print("CAMPUS EVENT FINANCIAL PLANNING")

venue_cost = float(input("Enter venue cost: "))
equipment_cost = float(input("Enter equipment cost: "))

catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

if (venue_cost < 0 or equipment_cost < 0 or
    catering < 0 or transport < 0 or certificate < 0 or
    participants < 0 or registration_fee < 0 or sponsorship < 0):

    print("Invalid input. Values cannot be negative.")

else:
    fixed_cost = venue_cost + equipment_cost

    cost_per_person = catering + transport + certificate

    total_cost = fixed_cost + (cost_per_person * participants)

    registration_income = registration_fee * participants

    total_income = registration_income + sponsorship

    profit_or_loss = total_income - total_cost

    print("\n--- EVENT FINANCIAL REPORT ---")
    print("Fixed Cost: Rs.", fixed_cost)
    print("Cost Per Participant: Rs.", cost_per_person)
    print("Total Event Cost: Rs.", total_cost)
    print("Registration Income: Rs.", registration_income)
    print("Sponsorship: Rs.", sponsorship)
    print("Total Income: Rs.", total_income)

    if profit_or_loss > 0:
        print("Event Surplus: Rs.", profit_or_loss)
    elif profit_or_loss < 0:
        print("Event Loss: Rs.", abs(profit_or_loss))
    else:
        print("The event breaks even.")

    if fixed_cost <= sponsorship:
        print("Minimum Participants for Break-even: 0")

    elif registration_fee > cost_per_person:
        contribution = registration_fee - cost_per_person
        remaining_cost = fixed_cost - sponsorship

        minimum_participants = (
            remaining_cost + contribution - 1
        ) // contribution

        print("Minimum Participants for Break-even:",
              minimum_participants)

    else:
        print("Break-even cannot be reached with the current")
        print("registration fee and sponsorship.")

8. Test Cases
Test	Participants	Registration Fee	Sponsorship	Expected Result
1	60	₹300	₹3,000	Surplus of ₹800
2	40	₹300	₹3,000	Loss of ₹800
3	50	₹300	₹3,000	Break-even
4	60	₹200	₹3,000	Break-even not possible with current fee
For all four tests, use these same costs:
Venue: ₹5,000
Equipment: ₹2,000
Catering per participant: ₹150
Transport per participant: ₹50
Certificate per participant: ₹20
9. Sample Input
Venue cost: 5000
Equipment cost: 2000
Catering cost per participant: 150
Transport cost per participant: 50
Certificate cost per participant: 20
Number of participants: 60
Registration fee per participant: 300
Sponsorship amount: 3000

10. Sample Output
CAMPUS EVENT FINANCIAL PLANNING

--- EVENT FINANCIAL REPORT ---
Fixed Cost: Rs. 7000.0
Cost Per Participant: Rs. 220.0
Total Event Cost: Rs. 20200.0
Registration Income: Rs. 18000.0
Sponsorship: Rs. 3000.0
Total Income: Rs. 21000.0
Event Surplus: Rs. 800.0
Minimum Participants for Break-even: 50

11. Output Screenshot
Open the Python program in IDLE, VS Code, or another Python editor.
Run Activity_10.py.
Enter the sample inputs.
Capture a screenshot showing the program and its output.
Save the screenshot in your project folder.
12. Conclusion
This project demonstrates how Python can be used to plan a campus event's finances. It calculates expenses, registration income, sponsorship, profit or loss, and the minimum number of participants required to break even. It uses basic variables, arithmetic operators, conditional statements, and input/output.
