# REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print("Before removing: ", pets)

while 'cat' in pets:
    pets.remove('cat')
print("After remvoing: ", pets)