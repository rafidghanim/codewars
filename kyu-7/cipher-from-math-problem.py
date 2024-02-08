def encrypt(word, n):
    encrypted_word = []

    if n < 0:
        n = 0  # Treat negative n as 0

    for c in word:
        alphabet_position = ord(c) - ord('a') + 1
        result = alphabet_position
        for i in range(n):
            result = result * 3 - 5
        encrypted_word.append(result)

    return encrypted_word

def decrypt(encrypted_word, n):
    decrypted_word = ''

    if n < 0:
        n = 0  # Treat negative n as 0

    for num in encrypted_word:
        result = num
        for i in range(n):
            result = (result + 5) // 3
        decrypted_char = chr(ord('a') + result - 1)
        decrypted_word += decrypted_char

    return decrypted_word
