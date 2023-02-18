[12:38, 18/02/2023] Stephustin: def rotate(text, key):
    """
    Rotates the characters in the given text by the given key. The rotation is done using
    a simple Caesar cipher algorithm, where each character is shifted forward in the alphabet
    by the given key. If the end of the alphabet is reached, the rotation continues from the
    beginning of the alphabet.

    :param text: The text to be rotated.
    :param key: The number of positions to rotate the characters by.
    :return: The rotated text.
    """
    result = ""

    # Iterate over each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Get the ASCII code of the character
            code = ord(char)

            # Calculate the new ASCII code after the rotation
            new_code = code + key

            # Check if the new code is outside the range of uppercase letters
            if char.isupper() and new_code > ord('Z'):
                new_code -= 26
            # Check if the new code is outside the range of lowercase letters
            elif char.islower() and new_code > ord('z'):
                new_code -= 26

            # Add the rotated character to the result
            result += chr(new_code)
        else:
            # If the character is not a letter, just add it to the result without rotating it
            result += char

    return result
plaintext = "Hello, world!"
key = 13
ciphertext = rotate(plaintext, key)
print(ciphertext)  # Outputs "Uryyb, jbeyq!"