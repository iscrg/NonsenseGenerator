def nonsense_generator(text, num_sentences):
    """
    The function generates a given number of rambling sentences and randomly inserts them into the original text.

    :param text: Normal text.
    :param num_sentences: The number of nonsense sentences you need to generate.
    :return: Nonsense text.
    """

    # Creating dictionary of text's words
    words = text.split()
    legacy_words = {}

    for i in range(len(text)-1):
        if text[i] in words.keys():
            legacy_words[text[i]].add(text[i+1])
        else:
            legacy_words[text[i]] = set(text[i+1])

    """
    Dict structure:
    
    legacy_words = {
        'word': set('legacy_words', 'word1', 'word2')
    }
    """


    # Generating sentences
    # Рандомно выбираем слово и после рандомно выбираем слово из тех, что могут идти после него. Делаем проверку, чтобы предолжение не было слишком длинным.
    nonsense_sentencies = []
    for i in range(num_sentences):
        nonsense_sentencies.append(None)

    # Placing sentences
    # Можно сделать сплит изначального текста по точками и рандомом определять после какого предложения ставить бредовые предложения.
    nonsense_text = None
    for i in range(num_sentences):
        pass

    return nonsense_text


with open('text.txt') as file:
    num_sentences = file.readline()
    text = file.read()

nonsense_text = nonsense_generator(text, num_sentences)

with open('nonsense_text.txt', 'w+') as file:
    file.write(nonsense_text)
