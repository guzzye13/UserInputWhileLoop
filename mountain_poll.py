responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")  # prompted to enter their name/mountain
    response = input("Which mountain would you like to climb? ")

    # Store the response in the dictionary.
    responses[name] = response  # information is stored in the responses dictionary.

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    # Asked to keep the poll running, if yes, program enters while loop.
    # If no, the polling_active flag is set to sale.
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n\t\t--- Poll Results ---")
for name, response in responses.items():  # Displays the results of the poll.
    print(name + " would like to climb " + response + ".")

