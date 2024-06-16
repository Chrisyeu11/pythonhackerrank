def getMoneySpent(keyboards, drives, b):
    # Initialize the maximum spendable amount as -1 (indicating no valid combination was found)
    max_spend = -1

    # Iterate over each keyboard
    for keyboard in keyboards:
        # Iterate over each drive
        for drive in drives:
            # Calculate the total cost for this keyboard and drive combination
            total_cost = keyboard + drive

            # Check if this cost is within the budget and greater than the current max spend
            if total_cost <= b and total_cost > max_spend:
                max_spend = total_cost

    # Return the maximum amount spent without exceeding the budget
    return max_spend
