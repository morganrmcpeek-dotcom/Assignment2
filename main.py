"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    return annual_cost/SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost/MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost/(CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost/credits/SEMESTERS_PER_YEAR


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return annual_cost*CS1430_CREDITS/SEMESTERS_PER_YEAR/CS1430_MEETINGS_PER_SEMESTER/credits


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits for this semester: "))

    while True:
        # Show your menu here.
        print("\nCOST OF COLLEGE")
        print("1 - Cost Per Semester")
        print("2 - Cost Per Month")
        print("3 - Cost Per Day")
        print("4 - Cost Per Credit")
        print("5 - Cost Per 1 CS1430 Class")
        print("6 - Is It Worth It?")
        print("Q - Quit")
        choice = input("Choose an option: ")

        if choice == "Q" or choice == "q":
            break
        elif choice == "1":
            print(f"\nOne semester of college costs: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"\nOne month of the academic year costs: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"\nOne day of college costs: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"\nOne credit costs: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"\nOne CS1430 class costs: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            expected_salary = float(input("Enter your expected annual salary after graduation: "))
            years_in_college = float(input("Enter the number of years you'll have been in college when you graduate: "))
            tuition_total = annual_cost * years_in_college
            pay_off_time = tuition_total / expected_salary
            print(f"\nYou'll pay off college in {pay_off_time:.1f} years.")
            if pay_off_time >= 15:
                print("That's way too long!")
            elif 10 <= pay_off_time < 15:
                print("That's alright for most.")
            elif 5 <= pay_off_time < 10:
                print("That's pretty good!")
            elif 0 <= pay_off_time < 5:
                print("Holy cow! You an engineer or something?")
        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
