import math

class PlayingCards:
    def __init__(self):
        self.cards = [
            "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
            "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
            "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH",
            "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"
        ]
        self.base = 27
        self.char_to_num = { ' ': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26 }
        self.num_to_char = { v: k for k, v in self.char_to_num.items() }
    
    def encode(self, message):
        num_value = 0
        for char in message:
            num_value = num_value * self.base + self.char_to_num[char]
        
        deck = self.cards[:]
        permutation = []
        
        for i in range(51, -1, -1):  
            factorial = math.factorial(i)
            index = num_value // factorial
            permutation.append(deck.pop(index))
            num_value = num_value % factorial
        
        return permutation
    
    def decode(self, deck):
        num_value = 0
        temp_deck = self.cards[:]
        
        for card in deck:
            index = temp_deck.index(card)
            num_value = num_value * len(temp_deck) + index
            temp_deck.remove(card)
        
        message = []
        while num_value > 0:
            message.append(self.num_to_char[num_value % self.base])
            num_value //= self.base
        
        return ''.join(reversed(message))
