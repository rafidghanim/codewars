class Cipher(object):
    def __init__(self, map1, map2):
        self.mapping = dict(zip(map1, map2))
    
    def encode(self, s):
        encoded = ""
        for char in s:
            if char in self.mapping:
                encoded += self.mapping[char]
            else:
                encoded += char
        return encoded
    
    def decode(self, s):
        decoded = ""
        reversed_mapping = {v: k for k, v in self.mapping.items()}
        for char in s:
            if char in reversed_mapping:
                decoded += reversed_mapping[char]
            else:
                decoded += char
        return decoded
