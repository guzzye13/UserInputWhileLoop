# THE WHILE LOOP IN ACTION
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""

# USING CONTINUE IN A LOOP
# use the continue statement to return to the beginning of the loop
# based on the result of a conditional test.
current_number = 0
while current_number < 10:
    current_number += 1  # If the modulo is 0 (divisible by 2)
    # the continue statement tells python to ignore the rest of the loop
    # and to return to the beginning.
    # If the current number is not divisible by 2, the rest of the loop
    # is executed and python prints the current number.
    if current_number % 2 == 0:
        continue
    print(current_number)


# AVOIDING INFINITE LOOPS
print("\nAvoiding infinite loops:")
x = 1
while x <= 5:
    print(x)
    x += 1
