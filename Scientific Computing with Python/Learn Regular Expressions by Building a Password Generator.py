import random
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
print(random.random())
"""
Step 9 
returns a floating point number in the range 
between 0.0 (inclusive) and 1.0 (exclusive).
ex)) print(random.random())

Step10
The choice() function from the random module takes 
a sequence and returns a random item of the sequence.

"""
