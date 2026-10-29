Problem Statement
Develop a Python program to calculate railway ticket fares based on travel distance, travel class, passenger age, and reservation charges. The program applies an age-based concession for senior passengers and displays the final ticket fare.
2. Objectives
To understand variables and data types in Python.
To perform fare calculations using arithmetic operators.
To use conditional statements to select travel-class rates.
To calculate age-based concessions.
To calculate reservation charges and the final fare.
To validate passenger inputs and display ticket details.
3. Concepts Used
Concept
Application
Variables
Store passenger details and fare amounts
Data types
Strings, integers, and floats
input()
Accept passenger information
int()
Convert age and distance into integers
float()
Store calculated fare amounts
Arithmetic operators
+, -, *, /
Comparison operators
>, <, >=, <=, ==
Logical operators
or
Conditional statements
if, elif, else
print()
Display ticket details
4. Assumptions
The following sample fare rules are used:
Travel class
Fare per kilometre
Reservation charge
Sleeper
₹1.50
₹40
AC
₹3.00
₹60
Additional assumptions:
The passenger enters the travel distance in kilometres.
The passenger selects either Sleeper or AC class.
Passengers aged 60 years or above receive a 20% concession on the basic fare.
Other passengers receive no age-based concession.
Reservation charges are added after calculating the concession.
Travel distance must be greater than zero.
Passenger age cannot be negative.
The program calculates the fare for one passenger.
These rates and concession rules are hypothetical and are used only for this educational project.
5. Algorithm
Start.
Enter the passenger's name.
Enter the travel distance.
Enter the passenger's age.
Enter the travel class.
Check whether the distance and age are valid.
Check whether the travel class is Sleeper or AC.
If the inputs are invalid, display an error message.
If the class is Sleeper, set the rate to ₹1.50 per kilometre and reservation charge to ₹40.
If the class is AC, set the rate to ₹3 per kilometre and reservation charge to ₹60.
Calculate the basic fare by multiplying distance by the applicable rate.
If the passenger is at least 60 years old, calculate a 20% concession on the basic fare.
Otherwise, set the concession to zero.
Calculate the final fare by subtracting the concession from the basic fare and adding the reservation charge.
Display the passenger details, basic fare, concession, reservation charge, and final fare.
Stop.
6. Flowchart
              ┌─────────────┐
              │    START    │
              └──────┬──────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Enter name, distance,   │
        │ age and travel class    │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Distance > 0 and        │
        │ age >= 0?               │
        └────────────┬────────────┘
                No   │   Yes
             ┌───────┘   └────────┐
             ▼                    ▼
     ┌────────────────┐    ┌─────────────────┐
     │ Invalid Input  │    │ Class Sleeper   │
     │                │    │ or AC?          │
     └────────┬───────┘    └────────┬────────┘
              │                     │
              │                     ▼
              │           ┌──────────────────┐
              │           │ Set class rate   │
              │           │ and reservation  │
              │           │ charge            │
              │           └────────┬─────────┘
              │                    │
              │                    ▼
              │           ┌──────────────────┐
              │           │ Calculate basic  │
              │           │ fare             │
              │           └────────┬─────────┘
              │                    │
              │                    ▼
              │           ┌──────────────────┐
              │           │ Age >= 60?       │
              │           └────────┬─────────┘
              │               Yes  │  No
              │             ┌──────┘ └────────┐
              │             ▼                 ▼
              │     ┌──────────────┐   ┌──────────────┐
              │     │ Concession = │   │ Concession  │
              │     │ Basic × 20%  │   │ = 0          │
              │     └──────┬───────┘   └──────┬───────┘
              │            │                  │
              │            └────────┬─────────┘
              │                     ▼
              │           ┌──────────────────┐
              │           │ Final fare =     │
              │           │ Basic - Discount │
              │           │ + Reservation    │
              │           └────────┬─────────┘
              │                    │
              │                    ▼
              │           ┌──────────────────┐
              │           │ Display ticket   │
              │           │ details and fare │
              │           └────────┬─────────┘
              │                    │
              └────────────────────┘
                                   ▼
                            ┌─────────────┐
                            │    STOP     │
                            └─────────────┘
7. Pseudocode
START

INPUT passenger_name
INPUT distance
INPUT age
INPUT travel_class

IF distance <= 0 OR age < 0 THEN
    DISPLAY "Invalid Input"

ELSE IF travel_class is not Sleeper or AC THEN
    DISPLAY "Invalid Travel Class"

ELSE
    IF travel_class = Sleeper THEN
        rate = 1.50
        reservation = 40
    ELSE
        rate = 3.00
        reservation = 60
    END IF

    basic_fare = distance * rate

    IF age >= 60 THEN
        concession = basic_fare * 0.20
    ELSE
        concession = 0
    END IF

    final_fare = basic_fare - concession + reservation

    DISPLAY passenger_name
    DISPLAY basic_fare
    DISPLAY concession
    DISPLAY reservation
    DISPLAY final_fare
END IF

STOP
8. Python Source Code
File name: Activity_6.py
# Railway Fare and Reservation Calculator

passenger_name = input("Enter passenger name: ")
distance = int(input("Enter travel distance in km: "))
age = int(input("Enter passenger age: "))
travel_class = input("Enter travel class (Sleeper/AC): ")

if distance <= 0 or age < 0:
    print("Invalid Input")

elif travel_class != "Sleeper" and travel_class != "AC":
    print("Invalid Travel Class")

else:
    if travel_class == "Sleeper":
        rate = 1.50
        reservation = 40

    else:
        rate = 3.00
        reservation = 60

    basic_fare = distance * rate

    if age >= 60:
        concession = basic_fare * 0.20

    else:
        concession = 0

    final_fare = basic_fare - concession + reservation

    print("\n--- Railway Ticket Details ---")
    print("Passenger Name:", passenger_name)
    print("Travel Distance:", distance, "km")
    print("Passenger Age:", age)
    print("Travel Class:", travel_class)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Age Concession: Rs.", round(concession, 2))
    print("Reservation Charge: Rs.", reservation)
    print("Final Ticket Fare: Rs.", round(final_fare, 2))
9. Test Cases
Test
Distance
Age
Class
Expected final fare
1
200 km
30
Sleeper
₹340
2
200 km
65
Sleeper
₹280
3
200 km
30
AC
₹660
4
100 km
60
AC
₹300
5
0 km
25
Sleeper
Invalid Input
6
100 km
25
General
Invalid Travel Class
7
100 km
-5
AC
Invalid Input
Sample calculations
Test 1: Sleeper class, age 30
Basic fare = 200 × ₹1.50 = ₹300
Concession = ₹0
Reservation charge = ₹40
Final fare = ₹300 − ₹0 + ₹40 = ₹340
Test 2: Sleeper class, age 65
Basic fare = 200 × ₹1.50 = ₹300
Concession = ₹300 × 20% = ₹60
Reservation charge = ₹40
Final fare = ₹300 − ₹60 + ₹40 = ₹280
Test 3: AC class, age 30
Basic fare = 200 × ₹3 = ₹600
Concession = ₹0
Reservation charge = ₹60
Final fare = ₹600 − ₹0 + ₹60 = ₹660
10. Sample Outputs
Output 1: Sleeper Class
Enter passenger name: Ravi
Enter travel distance in km: 200
Enter passenger age: 30
Enter travel class (Sleeper/AC): Sleeper

--- Railway Ticket Details ---
Passenger Name: Ravi
Travel Distance: 200 km
Passenger Age: 30
Travel Class: Sleeper
Basic Fare: Rs. 300.0
Age Concession: Rs. 0
Reservation Charge: Rs. 40
Final Ticket Fare: Rs. 340.0
Output 2: Senior Passenger
Enter passenger name: Ramesh
Enter travel distance in km: 200
Enter passenger age: 65
Enter travel class (Sleeper/AC): Sleeper

--- Railway Ticket Details ---
Passenger Name: Ramesh
Travel Distance: 200 km
Passenger Age: 65
Travel Class: Sleeper
Basic Fare: Rs. 300.0
Age Concession: Rs. 60.0
Reservation Charge: Rs. 40
Final Ticket Fare: Rs. 280.0
Output 3: AC Class
Enter passenger name: Priya
Enter travel distance in km: 200
Enter passenger age: 30
Enter travel class (Sleeper/AC): AC

--- Railway Ticket Details ---
Passenger Name: Priya
Travel Distance: 200 km
Passenger Age: 30
Travel Class: AC
Basic Fare: Rs. 600.0
Age Concession: Rs. 0
Reservation Charge: Rs. 60
Final Ticket Fare: Rs. 660.0
Output Screenshots
To create the actual screenshots required by your assignment:
Open Python IDLE or VS Code.
Save the code as Activity_6.py.
Run the program with the inputs from Test Cases 1, 2, and 3.
Capture screenshots showing the actual program output.
Save them with these suggested filenames:
output_1_sleeper_class.png
output_2_senior_concession.png
output_3_ac_class.png
These are suggested filenames. Capture the screenshots after running the program; the sample outputs above are not screenshots.
11. Conclusion
The Railway Fare and Reservation Calculator demonstrates how Python variables, arithmetic operators, and conditional statements can calculate ticket fares based on travel distance, class, and passenger age. It applies a sample senior concession, adds reservation charges, validates inputs, and displays the final ticket fare.
