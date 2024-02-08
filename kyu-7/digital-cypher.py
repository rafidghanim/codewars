def encode(message, key):
    key_digits = [int(digit) for digit in str(key)]
    key_cycle = [key_digits[i % len(key_digits)] for i in range(len(message))]
    return [(ord(char) - 96) + digit for char, digit in zip(message, key_cycle)]
