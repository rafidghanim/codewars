from preloaded import NATO # NATO['A'] == 'Alfa', etc

def to_nato(words : str) -> str:
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')
