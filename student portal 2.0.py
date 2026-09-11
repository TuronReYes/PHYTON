# ==========================================
#           STUDENT PORTAL SYSTEM
# ==========================================

# Variables for the registered account
registered_user = ""
registered_password = ""

# Student information
student_name = ""
student_section = ""


# ==========================================
#              REGISTRATION
# ==========================================

def register():

    global registered_user
    global registered_password
    global student_name
    global student_section

    print("\n================================")
    print("       STUDENT REGISTRATION")
    print("================================")

    student_name = input("Enter your Name: ")
    registered_user = input("Enter your Username: ")
    student_section = input("Enter your Section: ")

    registered_password = input("Enter your Password: ")
    confirm_password = input("Confirm your Password: ")

    if registered_password == confirm_password:

        if len(registered_password) >= 6:

            print("\nRegistration Successful!")
            print("Your account has been saved.")

            while True:

                print("\n================================")
                print("       AFTER REGISTRATION")
                print("================================")

                print("[1] Go Back to Portal")
                print("[2] Go Directly to Login")

                choice = input("\nEnter your choice: ")

                if choice == "1":
                    return "portal"

                elif choice == "2":
                    return "login"

                else:
                    print("Invalid choice!")

        else:
            print("\nPassword must be at least 6 characters!")

    else:
        print("\nPassword does not match!")

    return "portal"


# ==========================================
#                  LOGIN
# ==========================================

def login():

    if registered_user == "":
        print("\nNo account has been registered yet!")
        return False

    print("\n================================")
    print("             LOGIN")
    print("================================")

    login_user = input("Enter your Username: ")
    login_password = input("Enter your Password: ")

    if login_user == registered_user:

        if login_password == registered_password:

            print("\nLogin Successful!")
            print("Welcome,", student_name)

            return True

        else:
            print("\nIncorrect Password!")
            print("Login Failed!")

    else:
        print("\nUsername does not exist!")
        print("Login Failed!")

    return False


# ==========================================
#            STUDENT PROFILE
# ==========================================

def student_profile():

    while True:

        print("\n================================")
        print("        STUDENT PROFILE")
        print("================================")

        print("Name:", student_name)
        print("Username:", registered_user)
        print("Section:", student_section)

        print("\n[1] Go Back to Dashboard")
        print("[2] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            return "dashboard"

        elif choice == "2":
            return "logout"

        else:
            print("Invalid choice!")


# ==========================================
#                 CASHIER
# ==========================================

def cashier():

    while True:

        print("\n================================")
        print("             CASHIER")
        print("================================")

        print("[1] View Tuition Fee")
        print("[2] View Miscellaneous Fee")
        print("[3] Calculate Total")
        print("[4] Go Back to Dashboard")
        print("[5] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            tuition = 15000

            print("\nTuition Fee: ₱", tuition)

        elif choice == "2":

            miscellaneous = 3500

            print("\nMiscellaneous Fee: ₱", miscellaneous)

        elif choice == "3":

            tuition = 15000
            miscellaneous = 3500

            total = tuition + miscellaneous

            print("\nTuition Fee: ₱", tuition)
            print("Miscellaneous Fee: ₱", miscellaneous)
            print("Total Payment: ₱", total)

        elif choice == "4":

            return "dashboard"

        elif choice == "5":

            return "logout"

        else:
            print("Invalid choice!")


# ==========================================
#                   GRADE
# ==========================================

def grade():

    while True:

        print("\n================================")
        print("              GRADE")
        print("================================")

        print("[1] Calculate Grade")
        print("[2] Go Back to Dashboard")
        print("[3] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nEnter your grades:")

            math = float(input("Math: "))
            english = float(input("English: "))
            science = float(input("Science: "))

            average = (math + english + science) / 3

            print("\nAverage:", round(average, 2))

            if average >= 75:
                print("Status: PASSED")
            else:
                print("Status: FAILED")

        elif choice == "2":

            return "dashboard"

        elif choice == "3":

            return "logout"

        else:
            print("Invalid choice!")


# ==========================================
#                  LIBRARY
# ==========================================

def library():

    while True:

        print("\n================================")
        print("             LIBRARY")
        print("================================")

        print("[1] View Books")
        print("[2] Search Book")
        print("[3] Borrow Book")
        print("[4] Go Back to Dashboard")
        print("[5] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nAvailable Books:")

            print("[1] Python Programming")
            print("[2] Database Management")
            print("[3] Web Development")
            print("[4] Computer Fundamentals")
            print("[5] Information Technology")

        elif choice == "2":

            search = input("\nEnter book name: ").lower()

            if search == "python programming":
                print("Book Found: Python Programming")

            elif search == "database management":
                print("Book Found: Database Management")

            elif search == "web development":
                print("Book Found: Web Development")

            elif search == "computer fundamentals":
                print("Book Found: Computer Fundamentals")

            elif search == "information technology":
                print("Book Found: Information Technology")

            else:
                print("Book not found!")

        elif choice == "3":

            book = input("\nEnter the book you want to borrow: ")

            if book == "Python Programming":
                print("You borrowed:", book)

            elif book == "Database Management":
                print("You borrowed:", book)

            elif book == "Web Development":
                print("You borrowed:", book)

            elif book == "Computer Fundamentals":
                print("You borrowed:", book)

            elif book == "Information Technology":
                print("You borrowed:", book)

            else:
                print("Book is not available!")

        elif choice == "4":

            return "dashboard"

        elif choice == "5":

            return "logout"

        else:
            print("Invalid choice!")


# ==========================================
#            LOST & FOUND SYSTEM
# ==========================================

def lost_found():

    while True:

        print("\n================================")
        print("       LOST & FOUND SYSTEM")
        print("================================")

        print("[1] Report Lost Item")
        print("[2] Report Found Item")
        print("[3] Go Back to Dashboard")
        print("[4] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            item = input("\nEnter lost item: ")
            location = input("Where did you lose it? ")

            print("\nLost Item:", item)
            print("Location:", location)
            print("Lost item reported successfully!")

        elif choice == "2":

            item = input("\nEnter found item: ")
            location = input("Where did you find it? ")

            print("\nFound Item:", item)
            print("Location:", location)
            print("Found item reported successfully!")

        elif choice == "3":

            return "dashboard"

        elif choice == "4":

            return "logout"

        else:
            print("Invalid choice!")


# ==========================================
#       STUDENT DAILY BUDGET PLANNER
# ==========================================

def budget_planner():

    while True:

        print("\n================================")
        print("     DAILY BUDGET PLANNER")
        print("================================")

        print("[1] Create Daily Budget")
        print("[2] Go Back to Dashboard")
        print("[3] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            budget = float(input("\nEnter your daily budget: ₱"))

            food = float(input("Food expense: ₱"))
            transportation = float(input("Transportation expense: ₱"))
            school = float(input("School expense: ₱"))

            total_expense = food + transportation + school

            remaining = budget - total_expense

            print("\nTotal Expense: ₱", total_expense)
            print("Remaining Budget: ₱", remaining)

            if remaining >= 0:
                print("Status: Within Budget")
            else:
                print("Status: Over Budget")

        elif choice == "2":

            return "dashboard"

        elif choice == "3":

            return "logout"

        else:
            print("Invalid choice!")


# ==========================================
#            STUDENT SCHEDULE
# ==========================================

def schedule():

    while True:

        print("\n================================")
        print("        STUDENT SCHEDULE")
        print("================================")

        print("Monday    - Python Programming")
        print("Tuesday   - Mathematics")
        print("Wednesday - Database Management")
        print("Thursday  - Web Development")
        print("Friday    - Physical Education")

        print("\n[1] Go Back to Dashboard")
        print("[2] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            return "dashboard"

        elif choice == "2":

            return "logout"

        else:
            print("Invalid choice!")


# ==========================================
#                DASHBOARD
# ==========================================

def dashboard():

    while True:

        print("\n================================")
        print("        STUDENT DASHBOARD")
        print("================================")

        print("[1] Student Profile")
        print("[2] Cashier")
        print("[3] Grade")
        print("[4] Library")
        print("[5] Lost & Found System")
        print("[6] Student Daily Budget Planner")
        print("[7] Student Schedule")
        print("[8] Log Out")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            result = student_profile()

        elif choice == "2":

            result = cashier()

        elif choice == "3":

            result = grade()

        elif choice == "4":

            result = library()

        elif choice == "5":

            result = lost_found()

        elif choice == "6":

            result = budget_planner()

        elif choice == "7":

            result = schedule()

        elif choice == "8":

            return "logout"

        else:

            print("Invalid choice!")
            continue

        if result == "logout":

            return "logout"


# ==========================================
#              MAIN STUDENT PORTAL
# ==========================================

while True:

    print("\n================================")
    print("          STUDENT PORTAL")
    print("================================")

    print("[1] Register")
    print("[2] Login")
    print("[3] Exit")

    choice = input("\nEnter your choice: ")

    # --------------------------------------
    # REGISTER
    # --------------------------------------

    if choice == "1":

        result = register()

        # Directly go to login
        if result == "login":

            login_result = login()

            if login_result == True:

                dashboard_result = dashboard()

                if dashboard_result == "logout":
                    print("\nYou have been logged out.")

        # Go back to portal
        elif result == "portal":

            continue


    # --------------------------------------
    # LOGIN
    # --------------------------------------

    elif choice == "2":

        login_result = login()

        if login_result == True:

            dashboard_result = dashboard()

            if dashboard_result == "logout":

                print("\nYou have been logged out.")


    # --------------------------------------
    # EXIT
    # --------------------------------------

    elif choice == "3":

        print("\nThank you for using the Student Portal!")
        break


    # --------------------------------------
    # INVALID CHOICE
    # --------------------------------------

    else:

        print("\nInvalid choice!")