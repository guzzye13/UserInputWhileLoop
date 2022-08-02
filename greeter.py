prompt = "If you tell us who you are, we can personalize the messages you see."
# stores the first part of the message in the variable prompt.
prompt += "\nWhat is your first name? " # operator += takes the string
# that was stored in prompt and adds the new string onto the end.

name = input(prompt)
print("Hello " + name + "!")