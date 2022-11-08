def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # This will let us know if its a positive number
        # need to be sure its a number before converting to int
        if amount.isdigit():
            # need to convert the amount to an int
            amount = int(amount)
            if amount > 0:
                # if the amount is greater than 0, break out while loop
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount
