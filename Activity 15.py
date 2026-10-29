Develop a Python program to calculate parking fees based on vehicle type and parking duration. The program should include an overnight parking charge, apply a daily fee limit, and display the total parking fee.
2. Objectives
To understand Python variables and data types.
To accept vehicle and parking details from the user.
To calculate parking fees using arithmetic operators.
To apply conditions using if, elif, and else.
To develop a simple parking fee management system.
3. Assumptions
The following rates are assumed for this beginner-level project:
Car parking: ₹30 per hour.
Bike parking: ₹15 per hour.
Overnight parking charge: ₹100.
Maximum daily parking fee for a car: ₹300.
Maximum daily parking fee for a bike: ₹150.
Parking duration must be greater than zero.
For simplicity, the program considers one parking day and applies the daily limit to the hourly charge before adding any overnight charge.
These are sample rates for the project, not actual parking tariffs.
4. Algorithm
Start the program.
Enter the vehicle type.
Enter the number of parking hours.
Enter whether overnight parking is required.
Check whether the parking duration is valid.
If the vehicle is a car, calculate the fee at ₹30 per hour and apply the ₹300 daily limit.
If the vehicle is a bike, calculate the fee at ₹15 per hour and apply the ₹150 daily limit.
If overnight parking is selected, add ₹100.
Display the final parking fee.
Stop the program.
5. Flowchart
          START
            |
            v
   Enter vehicle type,
   parking hours and
   overnight choice
            |
            v
   Are parking hours
       greater than 0?
       /          \
     No            Yes
     |              |
     v              v
 Display         Is vehicle
 Invalid         a car?
 Duration        /      \
     |          Yes      No
     |           |        |
     |        Car fee   Bike fee
     |        = hours   = hours
     |        x 30      x 15
     |           |        |
     |        Apply     Apply
     |        ₹300      ₹150
     |        limit     limit
     |           |        |
     |           +---+----+
     |               |
     |               v
     |       Overnight selected?
     |           /       \
     |         Yes        No
     |          |          |
     |       Add ₹100      |
     |          |          |
     |          +----+-----+
     |               |
     |               v
     |       Display final fee
     |               |
     +---------------+
                     |
                     v
                    END
6. Pseudocode
START

INPUT vehicle_type
INPUT parking_hours
INPUT overnight

IF parking_hours <= 0
    DISPLAY "Invalid parking duration"

ELSE
    IF vehicle_type is "car"
        fee = parking_hours * 30

        IF fee > 300
            fee = 300
        END IF

    ELSE IF vehicle_type is "bike"
        fee = parking_hours * 15

        IF fee > 150
            fee = 150
        END IF

    ELSE
        DISPLAY "Invalid vehicle type"
    END IF

    IF vehicle type is valid
        IF overnight is "yes"
            fee = fee + 100
        END IF

        DISPLAY final parking fee
    END IF
END IF

STOP
7. Python Source Code
Save this program as Activity_15.py.
Writing
print("SMART PARKING FEE MANAGEMENT")
vehicle = input("Enter vehicle type (car/bike): ").lower() hours = int(input("Enter parking hours: ")) overnight = input("Overnight parking? (yes/no): ").lower()
if hours <= 0: print("Invalid parking duration")
elif vehicle == "car": fee = hours * 30
if fee > 300:
    fee = 300

if overnight == "yes":
    fee = fee + 100

print("Vehicle Type: Car")
print("Parking Fee: Rs.", fee)
elif vehicle == "bike": fee = hours * 15
if fee > 150:
    fee = 150

if overnight == "yes":
    fee = fee + 100

print("Vehicle Type: Bike")
print("Parking Fee: Rs.", fee)
else: print("Invalid vehicle type")
Explanation of Variables
Variable
Purpose
vehicle
Stores the vehicle type.
hours
Stores the number of parking hours.
overnight
Stores whether overnight parking is selected.
fee
Stores the calculated parking fee.
Conditions used:
if checks the parking duration and other conditions.
elif checks whether the vehicle is a car or a bike.
else displays an error for an invalid vehicle type.
Nested if statements apply the daily fee limit and overnight charge.
8. Test Cases
Test
Vehicle
Hours
Overnight
Expected Result
1
Car
2
No
₹60
2
Bike
3
No
₹45
3
Car
12
Yes
₹400
4
Bike
15
Yes
₹250
5
Car
0
No
Invalid parking duration
6
Bus
2
No
Invalid vehicle type
9. Output Screenshot
Sample Output
SMART PARKING FEE MANAGEMENT
Enter vehicle type (car/bike): car
Enter parking hours: 2
Overnight parking? (yes/no): no
Vehicle Type: Car
Parking Fee: Rs. 60
Screenshot instructions:
Run Activity_15.py in Python IDLE or VS Code.
Enter the sample inputs shown above.
Capture a screenshot showing the program and its output.
Save the screenshot as Activity_15_output.png.
Upload it to your Python ABL GitHub repository.
The output above is a sample; capture the actual screenshot after running the code.
10. Conclusion
The Smart Parking Fee Management program calculates parking charges based on vehicle type and parking duration. It uses variables, arithmetic operators, and conditional statements to apply parking rates, daily limits, and overnight charges. This project helps beginners understand how Python can solve simple real-world problems.
