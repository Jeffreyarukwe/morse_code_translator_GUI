from alphabet import alphabet


def encode(text):
    word_to_join = []
    for word in text:
        candidate_word = word.upper()
        if candidate_word not in alphabet.keys():
            continue
        word_to_join.append(alphabet[candidate_word])

    return " ".join(word_to_join)
