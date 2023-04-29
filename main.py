def calculator():
  while True:
    # Get the user's input
    user_input = input("Enter an equation (enter 'q' to quit): ")

    # If the user wants to quit, break out of the loop
    if user_input == 'q':
      break

    # Try to calculate the result
    try:
      result = eval(user_input)
    except Exception:
      print("Invalid equation")
      continue

    # Print the result
    print(result)

# Run the calculator
calculator()