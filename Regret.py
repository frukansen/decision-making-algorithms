def make_decision():

    situation = input("Are the inputs gains (g) or costs (c)? (g/c): ").lower()
    
    if situation not in ['g', 'c']:
        print("Invalid choice. Terminating the program.")
        return
    
    print("Enter the conditions (type 'q' to quit):")
    conditions = []
    while True:
        condition = input("Condition (type 'q' to quit): ")
        if condition.lower() == 'q':
            break
        conditions.append(condition)
    
    # Options
    print("\nEnter the options (type 'q' to quit):")
    options = []
    while True:
        option = input("Option (type 'q' to quit): ")
        if option.lower() == 'q':
            break
        options.append(option)
    
    print("\nEnter the results for each option under different conditions:")
    result_dict = {option: {} for option in options}
    for option in options:
        for condition in conditions:
            result = float(input(f"Enter the result of '{condition}' condition for option '{option}': "))
            result_dict[option][condition] = result
    
    total_regret = {option: 0 for option in options}
    
    for condition in conditions:
        # Results for all options under this condition
        condition_results = {option: result_dict[option][condition] for option in options}
        
        # Find the best option based on gains or costs
        if situation == 'g':  # Gain algorithm
            best_option = max(condition_results, key=condition_results.get)
        elif situation == 'c':  # Cost algorithm
            best_option = min(condition_results, key=condition_results.get)
        
        # Calculate regret values for other options
        for option in options:
            if option != best_option:
                # Regret: the difference between the possible best outcome and the chosen option.
                regret = abs(condition_results[option] - condition_results[best_option])
                total_regret[option] += regret
    
    # Choose the option with the least total regret
    choice = min(total_regret, key=total_regret.get)
    
    # Print results
    print("\nTotal regret values:")
    for option, regret in total_regret.items():
        print(f"{option}: {regret}")
    
    print(f"\nThe option with the least total regret: {choice}")

# Run the function
make_decision()
