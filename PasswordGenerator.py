import secrets
import string

def generate_password(length=12):
    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    # Make sure there is at least one character from each set
    password = [
        secrets.choice(uppercase_letters),
        secrets.choice(lowercase_letters),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]

    # Fill the rest of the password with random characters from all sets
    for _ in range(length - 4):
        password.append(secrets.choice(uppercase_letters + lowercase_letters + digits + special_chars))

    # Shuffle the password to ensure randomness
    secrets.SystemRandom().shuffle(password)

    # Convert the password list to a string
    password = ''.join(password)

    return password

# Generate and print a random password
password_length = 12
random_password = generate_password(password_length)
print("Generated password: ", random_password)

"""
The logic behind this password generator code can be explained as follows:

Import required modules:

secrets: A module for generating cryptographically secure random numbers. It's safer to use secrets than the random module when dealing with sensitive information like passwords.
string: A module containing various string constants, including character sets like ASCII letters, digits, and punctuation.
Define the generate_password function, which takes an optional length argument (default is 12):

Define the character sets:

uppercase_letters: Contains all the uppercase ASCII letters.
lowercase_letters: Contains all the lowercase ASCII letters.
digits: Contains all the digits from 0 to 9.
special_chars: Contains all the ASCII punctuation characters.
Make sure the password contains at least one character from each character set:

Use secrets.choice() to randomly choose one character from each set.
Add these characters to the password list.
Fill the rest of the password with random characters from all sets combined:

Concatenate all character sets.
Use a for loop to iterate length - 4 times (subtracting 4 because we've already added one character from each set).
In each iteration, use secrets.choice() to randomly choose a character from the combined character set and append it to the password list.
Shuffle the password list to ensure randomness:

Use secrets.SystemRandom().shuffle() to randomly shuffle the elements in the password list.
Convert the password list to a string:

Use the join() method to concatenate all characters in the password list into a single string.
Return the generated password string.

Generate and print a random password:

Call the generate_password() function, passing the desired password length (or using the default value of 12).
Print the generated password.
The result is a random password that meets the specified requirements, containing characters from uppercase letters, lowercase letters, digits, and special characters.

"""




