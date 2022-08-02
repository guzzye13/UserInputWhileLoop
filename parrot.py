#  LETTING THE USER CHOOSE WHEN TO QUIT
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit to end the program. "
message = ""  # set a variable message to store whatever value the user enters.
while message != "quit":  # while loop runs as long as the value is not 'quit'.
    message = input(prompt)
    # program makes sure there is no repeating word enter even
    # if it is 'quit'.
    if message != 'quit':
        print(message)