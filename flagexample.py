# USING A FLAG
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit to end the program. "

active = True  # program starts in active state
while active:  # As long as the active variable remains true,
    # the loop will continue running.
    message = input(prompt)

    if message == 'quit':  # once the loop is running, we check the value of the
        # message, if user enters 'quit' we set active to false, while loop ends.
        active = False
    else:  # if the user enters anything other than 'quit' we print the message.
        print(message)
