from alphabet import alphabet
from helper import get_key


def decode(text):
    word_to_join = []

    ciphertext = text.split("/")

    for i in range(len(ciphertext)):
        symbols = ciphertext[i].split()
        for symbol in symbols:
            if symbol not in alphabet.values():
                continue
            word_to_join.append(get_key(symbol))
        word_to_join.append(" ")

    return "".join(word_to_join)
