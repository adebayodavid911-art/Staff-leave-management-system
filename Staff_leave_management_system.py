leave_requests = []

def apply_leave():
    name = input("Enter staff name: ")
    days = input("Enter number of leave days: ")
    reason = input("Enter reason for leave: ")
    leave_requests.append({
        "name": name,
        "days": days,
        "reason": reason
    })
    print("Leave request submitted")

def view_leaves():
    if not leave_requests:
        print("No leave requests found")
    else:
        for l in leave_requests:
            print("Name:", l["name"])
            print("Days:", l["days"])
            print("Reason:", l["reason"])
            print("------------------")

def main():
    while True:
        print("1. Apply for Leave")
        print("2. View Leave Requests")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            apply_leave()
        elif choice == "2":
            view_leaves()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
