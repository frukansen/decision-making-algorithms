def equal_likelihood_criterion():
    print("Equal Likelihood Criterion Program")

    # Getting conditions from the user
    conditions = []
    print("\nEnter conditions (type 'done' to finish):")
    while True:
        condition = input("Condition: ").strip()
        if condition.lower() == "done":
            break
        if not condition:  # Exit if no condition is entered
            print("You entered an empty condition. Exiting the program.")
            return
        conditions.append(condition)

    # Exit if no conditions are entered
    if not conditions:
        print("No conditions entered. Exiting the program.")
        return

    # Getting options and their values from the user
    options = {}
    print("\nEnter options and their values for each condition:")
    while True:
        option = input("Option name (type 'done' to finish): ").strip()
        if option.lower() == "done":
            break
        if not option:  # Exit if no option is entered
            print("You entered an empty option. Exiting the program.")
            return

        option_values = []
        for condition in conditions:
            while True:
                try:
                    value = input(f"Enter the value for '{option}' for the condition '{condition}': ").strip()
                    if not value:  # Exit if no value is entered
                        print("You entered an empty value. Exiting the program.")
                        return
                    value = float(value)
                    option_values.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        options[option] = option_values

    # Exit if no options are entered
    if not options:
        print("No options entered. Exiting the program.")
        return

    # Calculating average values
    average_values = {
        option: sum(values) / len(values) for option, values in options.items()
    }

    # Finding the best option
    best_option = max(average_values, key=average_values.get)

    # Displaying the results
    print("\nResults:")
    for option, average in average_values.items():
        print(f"{option}: Average Value = {average:.2f}")
    print(f"\nThe best option: {best_option}")


# Run the program
equal_likelihood_criterion()
