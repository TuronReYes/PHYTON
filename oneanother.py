#Register Account Var
register_full_name = ""
register_username = ""
register_password = ""
register_section = ""

# Main Student Portal
while True:
    print("\n==============================")
    print("       STUDENT PORTAL")
    print("==============================")
    print("1. Register")
    print("2. Login")

    portal_choice = input("Enter your choice: ")

    #Register
    if portal_choice == "1":

        while True:
            print("\n==============================")
            print("     STUDENT REGISTRATION")
            print("==============================")

            register_full_name = input("Full Name: ").title()
            register_username = input("Username: ").lower()
            register_section = input("Section: ").title()
            register_password = input("Password: ").lower()
            confirm_password = input("Confirm Password: ").lower()

            # Check the required form
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

            #Check The Password Length
            if len(register_password) < 6:
                print("\n==============================")
                print("       INVALID PASSWORD")
                print("==============================")
                print("Password must be at least 6 characters.")
                continue

            #Check Password if Match
            if register_password != confirm_password:
                print("\n==============================")
                print("       PASSWORD MISMATCH")
                print("==============================")
                print("The passwords do not match.")
                print("Please enter the same password.")
                continue

            #Confirming the Information
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
                        portal_choice = "2"
                        break

                    elif register_choice == "2":
                        portal_choice = "0"
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

            # Go to login
            if portal_choice == "2":
                break

            # Back to portal
            if portal_choice == "0":
                break


        # Return to Portal if User Choose Back to Portal
        if portal_choice == "0":
            continue

    # Student Login System
    if portal_choice == "2":
        login_success = False

        while True:
            print("\n==============================")
            print("          STUDENT LOGIN")
            print("==============================")

            login_username = input("Username: ").lower()
            login_password = input("Password: ").lower()

            #Registered Student Login System
            if login_username == register_username:
                if login_password == register_password:
                    login_success = True

                    print("\nLogin successful!")
                    break

                else:
                    print("\n==============================")
                    print("          LOGIN FAILED")
                    print("==============================")
                    print("Wrong password.")

                    print("\n1. Try Again")
                    print("2. Back to Portal")

                    login_choice = input("Enter your choice: ")

                    if login_choice == "1":
                        continue

                    elif login_choice == "2":
                        break

                    else:
                        print("\nInvalid choice!")
                        print("Please choose 1 or 2.")

            #Account Not Found
            else:
                print("\n==============================")
                print("       ACCOUNT NOT FOUND")
                print("==============================")
                print("The username does not exist.")

                print("\n1. Try Again")
                print("2. Back to Portal")

                login_choice = input("Enter your choice: ")

                if login_choice == "1":
                    continue

                elif login_choice == "2":
                    break

                else:
                    print("\nInvalid choice!")
                    print("Please choose 1 or 2.")

        #Student Dashboard
        if login_success == True:

            while True:
                print("\n==============================")
                print("      STUDENT DASHBOARD")
                print("==============================")

                print("Welcome,", register_full_name)

                print("\n1. Student Profile")
                print("2. Cashier")
                print("3. Calculator")
                print("4. Library")
                print("5. Student Schedule")
                print("6. Log out")

                dashboard_choice = input("Enter your choice: ")

                #Student Profile
                if dashboard_choice == "1":

                    while True:
                        print("\n==============================")
                        print("       STUDENT PROFILE")
                        print("==============================")

                        print("Full Name :", register_full_name)
                        print("Username  :", register_username)
                        print("Section   :", register_section)

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

                # Cashier
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

                        #Tuition Fee
                        if cashier_choice == "1":

                            while True:
                                print("\n==============================")
                                print("        TUITION FEE")
                                print("==============================")

                                print("Student Name :", register_full_name)
                                print("Section      :", register_section)

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

                                tuition_choice = input("Enter your choice: ")

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

                        #Other Fees
                        elif cashier_choice == "2":

                            while True:
                                print("\n==============================")
                                print("          OTHER FEES")
                                print("==============================")

                                print("PRISAA       : ₱250.00")
                                print("College Days : ₱150.00")

                                print("\n1. Go back")
                                print("2. Log out")

                                other_fee_choice = input("Enter your choice: ")

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

                        #Back to Dashboard
                        elif cashier_choice == "3":
                            break

                        # LOG OUT
                        elif cashier_choice == "4":
                            login_success = False
                            break

                        else:
                            print("\nInvalid choice!")
                            print("Please choose 1 to 4.")

                    if login_success == False:
                        break


                # CALCULATOR
                elif dashboard_choice == "3":

                    while True:
                        print("\n==============================")
                        print("         CALCULATOR")
                        print("==============================")

                        print("1. Grade Calculator")
                        print("2. Calculator")
                        print("3. Go back to dashboard")
                        print("4. Log out")

                        calculator_choice = input("Enter your choice: ")

                        # GRADE CALCULATOR
                        if calculator_choice == "1":

                            while True:
                                print("\n==============================")
                                print("       GRADE CALCULATOR")
                                print("==============================")

                                print("\nEnter your grades.")
                                print("Leave blank if there is no grade.")
                                print("Blank grades will be counted as 0.\n")

                                rph_input = input("Readings in Philippine History: ")
                                if rph_input == "":
                                    rph = 0
                                else:
                                    rph = float(rph_input)

                                pathfit_input = input("Physical Activities Towards Health and Fitness: ")
                                if pathfit_input == "":
                                    pathfit = 0
                                else:
                                    pathfit = float(pathfit_input)

                                oral_input = input("Oral Communication: ")
                                if oral_input == "":
                                    oral = 0
                                else:
                                    oral = float(oral_input)

                                programming_input = input("Fundamentals of Programming: ")
                                if programming_input == "":
                                    programming = 0
                                else:
                                    programming = float(programming_input)

                                problem_solving_input = input("Fundamentals of Problem Solving: ")
                                if problem_solving_input == "":
                                    problem_solving = 0
                                else:
                                    problem_solving = float(problem_solving_input)

                                computing_input = input("Computing: ")
                                if computing_input == "":
                                    computing = 0
                                else:
                                    computing = float(computing_input)

                                mathematics_input = input("Mathematics in the Modern World: ")
                                if mathematics_input == "":
                                    mathematics = 0
                                else:
                                    mathematics = float(mathematics_input)

                                nstp_input = input("National Service Training Program 1: ")
                                if nstp_input == "":
                                    nstp = 0
                                else:
                                    nstp = float(nstp_input)

                                #Calculate Grade
                                total_grade = (rph + pathfit + oral + programming + problem_solving + computing + mathematics + nstp)
                                average = total_grade / 8

                                #Display Result
                                print("\n==============================")
                                print("        GRADE RESULT")
                                print("==============================")

                                print("Average:", average)

                                if average >= 98:
                                    print("Status: With Highest Honor")

                                elif average >= 95:
                                    print("Status: With High Honor")

                                elif average >= 90:
                                    print("Status: With Honor")

                                elif average >= 85:
                                    print("Status: Academic Awardee")

                                elif average >= 75:
                                    print("Status: Passed")

                                else:
                                    print("Status: Failed")

                                print("\n1. Try again")
                                print("2. Go back")
                                print("3. Log out")

                                grade_choice = input("Enter your choice: ")
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

                        #Normal Calculator
                        elif calculator_choice == "2":

                            while True:
                                print("\n==============================")
                                print("         CALCULATOR")
                                print("==============================")

                                num1 = int(input("Enter first number: "))
                                operator = input("Enter operator (+, -, *, /): ")
                                num2 = int(input("Enter second number: "))

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
                                        print("\nCannot divide by zero!")
                                    else:
                                        answer = num1 / num2
                                        print("\nResult:", answer)

                                else:
                                    print("\nInvalid operator!")
                                    print("Please use only +, -, * or /.")

                                print("\n1. Try again")
                                print("2. Go back")
                                print("3. Log out")

                                normal_choice = input("Enter your choice: ")

                                if normal_choice == "1":
                                    continue

                                elif normal_choice == "2":
                                    break

                                elif normal_choice == "3":
                                    login_success = False
                                    break

                                else:
                                    print("\nInvalid choice!")
                                    print("Please choose 1 to 3.")

                            if login_success == False:
                                break

                        #Back to Dashboard
                        elif calculator_choice == "3":
                            break

                        #Log Out
                        elif calculator_choice == "4":
                            login_success = False
                            break

                        else:
                            print("\nInvalid choice!")
                            print("Please choose 1 to 4.")

                    if login_success == False:
                        break

                #Library
                elif dashboard_choice == "4":

                    while True:
                        print("\n==============================")
                        print("           LIBRARY")
                        print("==============================")

                        print("1. View Books")
                        print("2. Borrow Book")
                        print("3. Go back to dashboard")
                        print("4. Log out")

                        library_choice = input("Enter your choice: ")

                        #View Books
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

                                view_book_choice = input("Enter your choice: ")

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

                        #Borrow Book
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

                                book_choice = input("\nEnter the book you want to borrow: ")

                                if book_choice == "1":
                                    borrowed_book = "Python Programming"

                                elif book_choice == "2":
                                    borrowed_book = "Computer Fundamentals"

                                elif book_choice == "3":
                                    borrowed_book = "Problem Solving"

                                elif book_choice == "4":
                                    borrowed_book = "NSTP"

                                else:
                                    print("\nInvalid book choice!")
                                    print("Please choose 1 to 4.")
                                    continue

                                print("\nYou borrowed:", borrowed_book)
                                break

                            print("\n1. Go back")
                            print("2. Log out")

                            borrow_choice = input("Enter your choice: ")

                            if borrow_choice == "1":
                                continue

                            elif borrow_choice == "2":
                                login_success = False
                                break

                            else:
                                print("\nInvalid choice!")
                                print("Please choose 1 or 2.")

                        #Back to Dashboard
                        elif library_choice == "3":
                            break

                        #Log out
                        elif library_choice == "4":
                            login_success = False
                            break

                        else:
                            print("\nInvalid choice!")
                            print("Please choose 1 to 4.")

                    if login_success == False:
                        break

                #Student Schedule
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

                        print("\nWednesday")
                        print("No classes")

                        print("\nThursday")
                        print("7:30 AM - 9:30 AM   - ACT 102")
                        print("9:30 AM - 11:30 AM  - ACT 103")

                        print("\nFriday")
                        print("8:00 AM - 9:30 AM   - ACT 101")
                        print("9:30 AM - 11:30 AM  - MMW")
                        print("11:30 AM - 1:00 PM   - NSTP")

                        print("\n1. Go back to dashboard")
                        print("2. Log out")

                        schedule_choice = input("Enter your choice: ")

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

                #Log out
                elif dashboard_choice == "6":
                    print("\n==============================")
                    print("       LOGOUT SUCCESSFUL")
                    print("==============================")
                    print("You have been logged out.")

                    login_success = False
                    break

                #Invalid Dashboard Choice
                else:
                    print("\nInvalid choice!")
                    print("Please choose 1 to 6.")

        # Return to Student Portal after logout
        if login_success == False:
            continue

    #Invalid Portal Choice
    else:
        print("\n==============================")
        print("       INVALID CHOICE")
        print("==============================")
        print("Please choose 1 or 2.")