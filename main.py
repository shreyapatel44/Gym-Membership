# GYM MEMBERSHIP CRUD SYSTEM

members = []

def add_member():
    print("\n--- Add New Member ---")
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    age = input("Enter Age: ")
    plan = input("Enter Membership Plan (Monthly/Quarterly/Yearly): ")

    member = {
        "ID": member_id,
        "Name": name,
        "Age": age,
        "Plan": plan
    }

    members.append(member)
    print("Member added successfully!")


def view_members():
    print("\n--- All Gym Members ---")
    if not members:
        print("No members found.")
    else:
        for m in members:
            print(f"ID: {m['ID']}, Name: {m['Name']}, Age: {m['Age']}, Plan: {m['Plan']}")


def search_member():
    print("\n--- Search Member ---")
    search_id = input("Enter Member ID to search: ")

    for m in members:
        if m["ID"] == search_id:
            print(f"\nMember Found!")
            print(f"ID: {m['ID']}")
            print(f"Name: {m['Name']}")
            print(f"Age: {m['Age']}")
            print(f"Plan: {m['Plan']}")
            return

    print("Member not found.")


def update_member():
    print("\n--- Update Member ---")
    update_id = input("Enter Member ID to update: ")

    for m in members:
        if m["ID"] == update_id:
            print(f"Current Name: {m['Name']}")
            new_name = input("Enter new name (leave blank to keep same): ")
            if new_name != "":
                m["Name"] = new_name

            print(f"Current Age: {m['Age']}")
            new_age = input("Enter new age (leave blank to keep same): ")
            if new_age != "":
                m["Age"] = new_age

            print(f"Current Plan: {m['Plan']}")
            new_plan = input("Enter new plan (leave blank to keep same): ")
            if new_plan != "":
                m["Plan"] = new_plan

            print("Member updated successfully!")
            return

    print("Member not found.")


def delete_member():
    print("\n--- Delete Member ---")
    delete_id = input("Enter Member ID to delete: ")

    for m in members:
        if m["ID"] == delete_id:
            members.remove(m)
            print("Member deleted successfully!")
            return

    print("Member not found.")


# MAIN PROGRAM LOOP
if __name__ == "__main__":
    while True:
        print("\n===== GYM MEMBERSHIP MANAGEMENT SYSTEM =====")
        print("1. Add Member")
        print("2. View All Members")
        print("3. Search Member")
        print("4. Update Member")
        print("5. Delete Member")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_member()
        elif choice == '2':
            view_members()
        elif choice == '3':
            search_member()
        elif choice == '4':
            update_member()
        elif choice == '5':
            delete_member()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
