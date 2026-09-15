# ==============================
# STUDENT PORTAL
# ==============================

# Fixed Login Account
fixed_full_name = "Anthony Ocampo"
fixed_username = "anthony"
fixed_password = "ocampo2026"
fixed_section = "ACT 1C"

# Registered Account
register_full_name = ""
register_username = ""
register_password = ""
register_section = ""

while True:

    print("\n==============================")
    print("       STUDENT PORTAL")
    print("==============================")
    print("1. Register")
    print("2. Login")

    portal_choice = input("Enter your choice: ")

    # ==============================
    # REGISTER
    # ==============================

    if portal_choice == "1":

        login_start = ""

        while True:

            print("\n==============================")
            print("     STUDENT REGISTRATION")
            print("==============================")

            register_full_name = input("Full Name: ").title()
            register_username = input("Username: ").lower()
            register_section = input("Section: ").title()
            register_password = input("Password: ").lower()
            confirm_password = input("Confirm Password: ").lower()

            # ==============================
            # CHECK REQUIRED INFORMATION
            # ==============================

            if register_full_name == "":
                print("\n==============================")
                print("   REGISTRATION INCOMPLETE")
                print("==============================")
                print("Full Name is required.")
                print("Please enter your full name.")
                continue

            if register_username == "":
                print("\n==============================")
                print("   REGISTRATION INCOMPLETE")
                print("==============================")
                print("Username is required.")
                print("Please enter a username.")
                continue

            if register_section == "":
                print("\n==============================")
                print("   REGISTRATION INCOMPLETE")
                print("==============================")
                print("Section is required.")
                print("Please enter your section.")
                continue

            if register_password == "":
                print("\n==============================")
                print("   REGISTRATION INCOMPLETE")
                print("==============================")
                print("Password is required.")
                print("Please enter a password.")
                continue

            if confirm_password == "":
                print("\n==============================")
                print("   REGISTRATION INCOMPLETE")
                print("==============================")
                print("Password confirmation is required.")
                print("Please confirm your password.")
                continue

            # ==============================
            # CHECK PASSWORD LENGTH
            # ==============================

            if len(register_password) < 6:
                print("\n==============================")
                print("       INVALID PASSWORD")
                print("==============================")
                print("Password must be at least 6 characters.")
                continue

            # ==============================
            # CHECK PASSWORD
            # ==============================

            if register_password != confirm_password:
                print("\n==============================")
                print("       PASSWORD MISMATCH")
                print("==============================")
                print("The passwords do not match.")
                print("Please enter the same password.")
                continue

            # ==============================
            # CONFIRM REGISTRATION
            # ==============================

            while True:

                print("\n==============================")
                print("     CONFIRM INFORMATION")
                print("==============================")
                print("Full Name :", register_full_name)
                print("Username  :", register_username)
                print("Section   :", register_section)
                print("Password  :", register_password)

                print("\nIs all the information correct?")
                print("1. Confirm Register")
                print("2. Change Information")

                confirm_choice = input("Enter your choice: ")

                if confirm_choice == "1":

                    print("\n==============================")
                    print("   REGISTRATION SUCCESSFUL")
                    print("==============================")
                    print("Your student account has been registered.")

                    print("\nWhat do you want to do?")
                    print("1. Go to Login")
                    print("2. Back to Portal")

                    register_choice = input("Enter your choice: ")

                    if register_choice == "1":

                        login_start = True
                        break

                    elif register_choice == "2":

                        login_start = False
                        break

                    else:

                        print("\nInvalid choice!")
                        print("Please choose 1 or 2.")

                elif confirm_choice == "2":

                    print("\nPlease enter your information again.")
                    break

                else:

                    print("\nInvalid choice!")
                    print("Please choose 1 or 2.")

            # If user wants to login
            if login_start == True:
                break

            # If user wants to return to portal
            if login_start == False:
                break

        # If user selected Go to Login
        if login_start == True:
            portal_choice = "2"

        # If user selected Back to Portal
        else:
            continue

    # ==============================
    # LOGIN
    # ==============================

    if portal_choice == "2":

        login_success = False

        # ==============================
        # LOGIN TRY AGAIN LOOP
        # ==============================

        while True:

            print("\n==============================")
            print("          STUDENT LOGIN")
            print("==============================")

            login_username = input("Username: ").lower()
            login_password = input("Password: ").lower()

            # ==============================
            # CHECK FIXED ACCOUNT
            # ==============================

            if login_username == fixed_username:

                if login_password == fixed_password.lower():

                    login_success = True

                    current_full_name = fixed_full_name
                    current_username = fixed_username
                    current_section = fixed_section

                    print("\nLogin successful!")
                    break

                else:

                    print("\n==============================")
                    print("          LOGIN FAILED")
                    print("==============================")
                    print("Wrong password!")

                    print("\n[1] Try Again")
                    print("[2] Back to Portal")

                    login_choice = input("Enter your choice: ")

                    if login_choice == "1":

                        continue

                    elif login_choice == "2":

                        break

                    else:

                        print("\nInvalid choice!")
                        print("Please choose 1 or 2.")

            # ==============================
            # CHECK REGISTERED ACCOUNT
            # ==============================

            elif login_username == register_username:

                if login_password == register_password:

                    login_success = True

                    current_full_name = register_full_name
                    current_username = register_username
                    current_section = register_section

                    print("\nLogin successful!")
                    break

                else:

                    print("\n==============================")
                    print("          LOGIN FAILED")
                    print("==============================")
                    print("Wrong password!")

                    print("\n[1] Try Again")
                    print("[2] Back to Portal")

                    login_choice = input("Enter your choice: ")

                    if login_choice == "1":

                        continue

                    elif login_choice == "2":

                        break

                    else:

                        print("\nInvalid choice!")
                        print("Please choose 1 or 2.")

            # ==============================
            # ACCOUNT NOT FOUND
            # ==============================

            else:

                print("\n==============================")
                print("       ACCOUNT NOT FOUND")
                print("==============================")
                print("The username does not exist.")

                print("\n[1] Try Again")
                print("[2] Back to Portal")

                login_choice = input("Enter your choice: ")

                if login_choice == "1":

                    continue

                elif login_choice == "2":

                    break

                else:

                    print("\nInvalid choice!")
                    print("Please choose 1 or 2.")

        # ==============================
        # STUDENT DASHBOARD
        # ==============================

        if login_success == True:

            current_full_name = register_full_name
            current_username = register_username
            current_section = register_section

            while True:

                print("\n==============================")
                print("      STUDENT DASHBOARD")
                print("==============================")
                print("Welcome,", current_full_name)

                print("\n1. Student Profile")
                print("2. Cashier")
                print("3. Calculator")
                print("4. Library")
                print("5. Student Schedule")
                print("6. Log out")

                dashboard_choice = input("Enter your choice: ")

                # ==============================
                # STUDENT PROFILE
                # ==============================

                if dashboard_choice == "1":

                    while True:

                        print("\n==============================")
                        print("       STUDENT PROFILE")
                        print("==============================")

                        print("Full Name :", current_full_name)
                        print("Username  :", current_username)
                        print("Section   :", current_section)

                        print("\n1. Go back to dashboard")
                        print("2. Log out")

                        profile_choice = input("Enter your choice: ")

                        if profile_choice == "1":

                            break

                        elif profile_choice == "2":

                            login_success = False
                            break

                        else:

                            print("\nInvalid choice!")
                            print("Please choose 1 or 2.")

                    if login_success == False:
                        break

                # ==============================
                # CASHIER
                # ==============================

                elif dashboard_choice == "2":

                    while True:

                        print("\n==============================")
                        print("           CASHIER")
                        print("==============================")

                        print("1. View Tuition Fee")
                        print("2. Other Fees")
                        print("3. Go back to dashboard")
                        print("4. Log out")

                        cashier_choice = input("Enter your choice: ")

                        # ==============================
                        # TUITION FEE
                        # ==============================

                        if cashier_choice == "1":

                            while True:

                                print("\n==============================")
                                print("        TUITION FEE")
                                print("==============================")

                                print("Student Name:", current_full_name)
                                print("Section     :", current_section)
                                print("Tuition Fee Balance: ₱10,985.00")

                                print("\nTuition Fee Breakdown")
                                print("------------------------------")
                                print("July       : ₱2,197.00")
                                print("August     : ₱2,197.00")
                                print("September  : ₱2,197.00")
                                print("October    : ₱2,197.00")
                                print("November   : ₱2,197.00")

                                print("\n1. Go back")
                                print("2. Log out")

                                tuition_choice = input(
                                    "Enter your choice: "
                                )

                                if tuition_choice == "1":

                                    break

                                elif tuition_choice == "2":

                                    login_success = False
                                    break

                                else:

                                    print("\nInvalid choice!")
                                    print("Please choose 1 or 2.")

                            if login_success == False:
                                break

                        # ==============================
                        # OTHER FEES
                        # ==============================

                        elif cashier_choice == "2":

                            while True:

                                print("\n==============================")
                                print("          OTHER FEES")
                                print("==============================")

                                print("PRISAA       : ₱250.00")
                                print("College Days : ₱150.00")

                                print("\n1. Go back")
                                print("2. Log out")

                                other_fee_choice = input(
                                    "Enter your choice: "
                                )

                                if other_fee_choice == "1":

                                    break

                                elif other_fee_choice == "2":

                                    login_success = False
                                    break

                                else:

                                    print("\nInvalid choice!")
                                    print("Please choose 1 or 2.")

                            if login_success == False:
                                break

                        # ==============================
                        # CASHIER BACK TO DASHBOARD
                        # ==============================

                        elif cashier_choice == "3":

                            break

                        # ==============================
                        # CASHIER LOGOUT
                        # ==============================

                        elif cashier_choice == "4":

                            login_success = False
                            break

                        else:

                            print("\nInvalid choice!")
                            print("Please choose 1 to 4.")

                    if login_success == False:
                        break

                # ==============================
                # CALCULATOR
                # ==============================

                elif dashboard_choice == "3":

                    while True:

                        print("\n==============================")
                        print("         CALCULATOR")
                        print("==============================")

                        print("1. Grade Calculator")
                        print("2. Calculator")
                        print("3. Go back to dashboard")
                        print("4. Log out")

                        calculator_menu_choice = input(
                            "Enter your choice: "
                        )

                        # ==============================
                        # GRADE CALCULATOR
                        # ==============================

                        if calculator_menu_choice == "1":

                            while True:

                                print("\n==============================")
                                print("       GRADE CALCULATOR")
                                print("==============================")

                                print("\nEnter your grades.")
                                print("Leave blank if there is no grade.")
                                print("Blank grades will be counted as 0.\n")

                                rph_input = input(
                                    "Readings in Philippine History: "
                                )

                                if rph_input == "":
                                    rph = 0
                                else:
                                    rph = float(rph_input)

                                pathfit_input = input(
                                    "Physical Activities Towards Health and Fitness: "
                                )

                                if pathfit_input == "":
                                    pathfit = 0
                                else:
                                    pathfit = float(pathfit_input)

                                oral_input = input(
                                    "Oral Communication: "
                                )

                                if oral_input == "":
                                    oral = 0
                                else:
                                    oral = float(oral_input)

                                programming_input = input(
                                    "Fundamentals of Programming: "
                                )

                                if programming_input == "":
                                    programming = 0
                                else:
                                    programming = float(programming_input)

                                problem_solving_input = input(
                                    "Fundamentals of Problem Solving: "
                                )

                                if problem_solving_input == "":
                                    problem_solving = 0
                                else:
                                    problem_solving = float(
                                        problem_solving_input
                                    )

                                computing_input = input(
                                    "Computing: "
                                )

                                if computing_input == "":
                                    computing = 0
                                else:
                                    computing = float(computing_input)

                                mathematics_input = input(
                                    "Mathematics in the Modern World: "
                                )

                                if mathematics_input == "":
                                    mathematics = 0
                                else:
                                    mathematics = float(
                                        mathematics_input
                                    )

                                nstp_input = input(
                                    "National Service Training Program 1: "
                                )

                                if nstp_input == "":
                                    nstp = 0
                                else:
                                    nstp = float(nstp_input)

                                # ==============================
                                # CALCULATE AVERAGE
                                # ==============================

                                total_grade = (
                                    rph
                                    + pathfit
                                    + oral
                                    + programming
                                    + problem_solving
                                    + computing
                                    + mathematics
                                    + nstp
                                )

                                average = total_grade / 8

                                print("\n==============================")
                                print("        GRADE RESULT")
                                print("==============================")

                                print("Average:", average)

                                if average >= 98:

                                    print(
                                        "Status: With Highest Honor"
                                    )

                                elif average >= 95:

                                    print(
                                        "Status: With High Honor"
                                    )

                                elif average >= 90:

                                    print(
                                        "Status: With Honor"
                                    )

                                elif average >= 85:

                                    print(
                                        "Status: Academic Awardee"
                                    )

                                elif average >= 75:

                                    print(
                                        "Status: Passed"
                                    )

                                else:

                                    print(
                                        "Status: Failed"
                                    )

                                print("\n1. Try again")
                                print("2. Go back")
                                print("3. Log out")

                                grade_choice = input(
                                    "Enter your choice: "
                                )

                                if grade_choice == "1":

                                    continue

                                elif grade_choice == "2":

                                    break

                                elif grade_choice == "3":

                                    login_success = False
                                    break

                                else:

                                    print("\nInvalid choice!")
                                    print("Please choose 1 to 3.")

                            if login_success == False:
                                break

                        # ==============================
                        # NORMAL CALCULATOR
                        # ==============================

                        elif calculator_menu_choice == "2":

                            while True:

                                print("\n==============================")
                                print("         CALCULATOR")
                                print("==============================")

                                num1 = int(
                                    input("Enter first number: ")
                                )

                                operator = input(
                                    "Enter operator (+, -, *, /): "
                                )

                                num2 = int(
                                    input("Enter second number: ")
                                )

                                if operator == "+":

                                    answer = num1 + num2
                                    print("\nResult:", answer)

                                elif operator == "-":

                                    answer = num1 - num2
                                    print("\nResult:", answer)

                                elif operator == "*":

                                    answer = num1 * num2
                                    print("\nResult:", answer)

                                elif operator == "/":

                                    if num2 == 0:

                                        print(
                                            "\nCannot divide by zero!"
                                        )

                                    else:

                                        answer = num1 / num2
                                        print("\nResult:", answer)

                                else:

                                    print("\nInvalid operator!")
                                    print(
                                        "Please use only +, -, * or /."
                                    )

                                print("\n1. Try again")
                                print("2. Go back")
                                print("3. Log out")

                                normal_calculator_choice = input(
                                    "Enter your choice: "
                                )

                                if normal_calculator_choice == "1":

                                    continue

                                elif normal_calculator_choice == "2":

                                    break

                                elif normal_calculator_choice == "3":

                                    login_success = False
                                    break

                                else:

                                    print("\nInvalid choice!")
                                    print("Please choose 1 to 3.")

                            if login_success == False:
                                break

                        # ==============================
                        # CALCULATOR BACK TO DASHBOARD
                        # ==============================

                        elif calculator_menu_choice == "3":

                            break

                        # ==============================
                        # CALCULATOR LOGOUT
                        # ==============================

                        elif calculator_menu_choice == "4":

                            login_success = False
                            break

                        else:

                            print("\nInvalid choice!")
                            print("Please choose 1 to 4.")

                    if login_success == False:
                        break

                # ==============================
                # LIBRARY
                # ==============================

                elif dashboard_choice == "4":

                    while True:

                        print("\n==============================")
                        print("           LIBRARY")
                        print("==============================")

                        print("1. View Books")
                        print("2. Borrow Book")
                        print("3. Go back to dashboard")
                        print("4. Log out")

                        library_choice = input(
                            "Enter your choice: "
                        )

                        # ==============================
                        # VIEW BOOKS
                        # ==============================

                        if library_choice == "1":

                            while True:

                                print("\n==============================")
                                print("          BOOK LIST")
                                print("==============================")

                                print("1. Python Programming")
                                print("2. Computer Fundamentals")
                                print("3. Problem Solving")
                                print("4. NSTP")

                                print("\n1. Go back")
                                print("2. Log out")

                                view_book_choice = input(
                                    "Enter your choice: "
                                )

                                if view_book_choice == "1":

                                    break

                                elif view_book_choice == "2":

                                    login_success = False
                                    break

                                else:

                                    print("\nInvalid choice!")
                                    print("Please choose 1 or 2.")

                            if login_success == False:
                                break

                        # ==============================
                        # BORROW BOOK
                        # ==============================

                        elif library_choice == "2":

                            while True:

                                print("\n==============================")
                                print("         BORROW BOOK")
                                print("==============================")

                                print("Available Books:")
                                print("1. Python Programming")
                                print("2. Computer Fundamentals")
                                print("3. Problem Solving")
                                print("4. NSTP")

                                book_choice = input(
                                    "\nEnter the book you want to borrow: "
                                )

                                if book_choice == "1":

                                    borrowed_book = "Python Programming"

                                    print(
                                        "\nYou borrowed:",
                                        borrowed_book
                                    )
                                    break

                                elif book_choice == "2":

                                    borrowed_book = (
                                        "Computer Fundamentals"
                                    )

                                    print(
                                        "\nYou borrowed:",
                                        borrowed_book
                                    )
                                    break

                                elif book_choice == "3":

                                    borrowed_book = "Problem Solving"

                                    print(
                                        "\nYou borrowed:",
                                        borrowed_book
                                    )
                                    break

                                elif book_choice == "4":

                                    borrowed_book = "NSTP"

                                    print(
                                        "\nYou borrowed:",
                                        borrowed_book
                                    )
                                    break

                                else:

                                    print(
                                        "\nInvalid book choice!"
                                    )
                                    print("Please choose 1 to 4.")

                            if login_success == False:
                                break

                            print("\n1. Go back")
                            print("2. Log out")

                            borrow_choice = input(
                                "Enter your choice: "
                            )

                            if borrow_choice == "1":

                                continue

                            elif borrow_choice == "2":

                                login_success = False
                                break

                            else:

                                print("\nInvalid choice!")
                                print("Please choose 1 or 2.")

                        # ==============================
                        # LIBRARY BACK TO DASHBOARD
                        # ==============================

                        elif library_choice == "3":

                            break

                        # ==============================
                        # LIBRARY LOGOUT
                        # ==============================

                        elif library_choice == "4":

                            login_success = False
                            break

                        else:

                            print("\nInvalid choice!")
                            print("Please choose 1 to 4.")

                    if login_success == False:
                        break

                # ==============================
                # STUDENT SCHEDULE
                # ==============================

                elif dashboard_choice == "5":

                    while True:

                        print("\n==============================")
                        print("       STUDENT SCHEDULE")
                        print("==============================")

                        print("\nMonday")
                        print("No classes")

                        print("\nTuesday")
                        print("8:00 AM - 10:00 AM   - RPH")
                        print("10:00 AM - 11:30 AM  - Subject")
                        print("11:30 AM - 1:00 PM   - PATHFIT")

                        print("\n1. Go back to dashboard")
                        print("2. Log out")

                        schedule_choice = input(
                            "Enter your choice: "
                        )

                        if schedule_choice == "1":

                            break

                        elif schedule_choice == "2":

                            login_success = False
                            break

                        else:

                            print("\nInvalid choice!")
                            print("Please choose 1 or 2.")

                    if login_success == False:
                        break

                # ==============================
                # LOGOUT
                # ==============================

                elif dashboard_choice == "6":

                    print("\n==============================")
                    print("       LOGOUT SUCCESSFUL")
                    print("==============================")
                    print("You have been logged out.")

                    login_success = False
                    break

                else:

                    print("\nInvalid choice!")
                    print("Please choose 1 to 6.")

        # ==============================
        # AFTER LOGOUT
        # RETURN TO STUDENT PORTAL
        # ==============================

        if login_success == False:
            continue

    # ==============================
    # INVALID PORTAL CHOICE
    # ==============================

    else:

        print("\n==============================")
        print("       INVALID CHOICE")
        print("==============================")
        print("Please choose 1 or 2.")