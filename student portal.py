print("==============================")
print("   STUDENT PORTAL")
print("==============================")

register_user = ""
register_password = ""
account = False

print("[1] Register")
print("[2] Already have an account")
student_portal_choice = int(input("\nEnter your choice: "))

account = False
if student_portal_choice == 1:
    print("\n==============================")
    print("   STUDENT REGISTRATION PORTAL")
    print("==============================")

    student_full_name = input("Enter your Full Name: ").upper()
    register_username = input("Enter your Username: ").upper()
    student_section = input("Enter your Section: ").upper()
    register_password = input("Enter your Password: ").upper()
    register_conf_pass = input("Confirm your Password: ").upper()


    if register_password == register_conf_pass:
        if len(register_password) >= 6:
            print("Congratulations! You have successfully Created!")
            print(f"Username: {register_username}")
            account = True

            print("\n==============================")
            print("   STUDENT LOG IN PORTAL")
            print("==============================")
            login_username = input("Enter your Username: ").upper()
            login_password = input("Enter your Password: ").upper()

            if login_username == register_username:
                if login_password == register_password:
                    print("Login Successful!")
                else:
                    print("Password Incorrect!")
            else:
                print("Incorrect Username!")

            print("\n==============================")
            print("   STUDENT DASHBOARD ")
            print(f"Welcome {student_full_name}!")
            print("==============================")

        else:
            print("Password too short! Must at least 6 characters!")

    else:
        print("Password In match!")

elif student_portal_choice == 2:
    print("\n==============================")
    print("   STUDENT LOG IN PORTAL")
    print("==============================")
    fixed_full_name = "ANTHONY OCAMPO"
    fixed_login_username = "ANTHONY"
    fixed_login_password = "OCAMPO2026"

    login_username = input("Enter your Username: ").upper()
    login_password = input("Enter your Password: ").upper()
    if login_username == fixed_login_username:
        if login_password == fixed_login_password:
            print("Login Successful!")
        else:
            print("Password Incorrect!")
    else:
        print("Incorrect Username!")

    print("\n==============================")
    print("    STUDENT DASHBOARD ")
    print(f"Welcome {fixed_full_name}!")
    print("==============================")


else:
    print("Invalid Choice!")







