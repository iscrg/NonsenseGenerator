'''
Fisher D. - 100
Fedyakin D. - 75
Popov I. - 90
'''

import random


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

    for i in range(len(words)-1):
        if words[i] in legacy_words.keys():
            legacy_words[words[i]].append(words[i+1])
        else:
            legacy_words[words[i]] = [words[i+1]]

    # Generating sentences and text
    nonsense_text = ''
    for i in range(num_sentences):
        word = random.choice(list(legacy_words.keys()))
        nonsense_sentence = word + ' '
        words_amount = 1

        while words_amount <= 30 and not(word[-1] in '.!?'):
            word = random.choice(legacy_words[word])
            nonsense_sentence += word + ' '
            words_amount += 1
        
        if nonsense_sentence[-2] not in '.!?':
            nonsense_sentence = nonsense_sentence[:-1] + '. '
        
        nonsense_text += nonsense_sentence
    
    return nonsense_text


with open('text.txt') as file:
    num_sentences = int(file.readline())
    text = file.read()

nonsense_text = nonsense_generator(text, num_sentences)

with open('nonsense_text.txt', 'w+', encoding='utf-8') as file:
    file.write(nonsense_text)
