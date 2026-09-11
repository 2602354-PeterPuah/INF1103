inventory=0
failed_entries=0

while True:
    user_input = input("Enter stock quantity: ")

    # Stop the program if user types quit
    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a non-negative integer.")
        failed_entries += 1
        continue

    stock=int(user_input)

    inventory += stock

    print(f"Current inventory: ", inventory)

    if inventory > 500:
        print("Inventory exceeded 500 units!!")
        break

print("Totals Units Processed: ", inventory)
print("Number of failed entries:")