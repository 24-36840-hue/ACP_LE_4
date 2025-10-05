import os



doc_path = os.path.expanduser("~/Documents")



if not os.path.exists(doc_path):

    os.makedirs(doc_path)



def register_student():

    """Register a student and save their record into a text file."""

    print("\n--- Register Student ---")

    student_no = input("Enter Student No.: ")



    # Collect details

    last_name = input("Enter Last Name: ")

    first_name = input("Enter First Name: ")

    middle_initial = input("Enter Middle Initial: ")

    program = input("Enter Program: ")

    age = input("Enter Age: ")

    gender = input("Enter Gender: ")

    birthday = input("Enter Birthday (MM/DD/YYYY): ")

    contact_no = input("Enter Contact No.: ")



    # Organize details in a list

    data = [

        f"Student No.: {student_no}",

        f"Full Name: {last_name}, {first_name} {middle_initial}.",

        f"Program: {program}",

        f"Age: {age}",

        f"Gender: {gender}",

        f"Birthday: {birthday}",

        f"Contact No.: {contact_no}"

    ]



    # File path for the student record

    file_path = os.path.join(doc_path, student_no + ".txt")



    # Write to file

    with open(file_path, "w") as f:

        for line in data:

            f.write(line + "\n")



    print(f"✅ Student record for {student_no} has been saved.\n")





def open_student_record():

    """Open and display a student record file."""

    print("\n--- Open Student Record ---")

    student_no = input("Enter Student No.: ")

    file_path = os.path.join(doc_path, student_no + ".txt")



    try:

        with open(file_path, "r") as f:

            print("\n📄 Student Record:")

            for line in f:

                print(line.strip())

    except FileNotFoundError:

        print("❌ Student record not found.\n")





def main_menu():

    """Main menu loop for the program."""

    while True:

        print("\n===== Student Records Management =====")

        print("1. Register Student")

        print("2. Open Student Record")

        print("3. Exit")

        choice = input("Enter your choice: ")



        if choice == "1":

            register_student()

        elif choice == "2":

            open_student_record()

        elif choice == "3":

            print("👋 Goodbye! Thank you for using the program.")

            break

        else:

            print("⚠️ Invalid choice. Please try again.\n")





# Run the program

if __name__ == "__main__":

    main_menu()

