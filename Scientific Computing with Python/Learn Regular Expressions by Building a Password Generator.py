#Learn Regular Expressions by Building a Password Generator
import random
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)

"""
Step 9 
returns a floating point number in the range 
between 0.0 (inclusive) and 1.0 (exclusive).
ex)) print(random.random()) #0.6309669497757615

Step10
The choice() function from the random module takes 
a sequence and returns a random item of the sequence.
ex)) print(random.choice(all_characters)) #임의 숫자 하나 발생

Step11
렌덤은 예측이 가능하다. 
instead of importing random, import the secrets module. 
Then change the print() call to use secrets.choice(all_characters).


"""
