
def adjectives():
    adjective = ["young"]
    for word in adjective:
        yield word

def determiners():
    determiner = ["the", "a"]
    for word in determiner:
        yield word

def nouns():
    noun = ["boy", "song"]
    for word in noun:
        yield word

def verbs():
    verb = ["sings"]
    for word in verb:
        yield word

def verb_phrases():
    for verb in verbs():
        yield verb
    for verb in verbs():
        for noun_phrase in noun_phrases():
            yield verb + " " + noun_phrase

def noun_phrases2():
    for adjective in adjectives():
        for noun in nouns():
            yield adjective + " " + noun
    for noun in nouns():
        yield noun

def noun_phrases():
    for determiner in determiners():
        for noun_phrase in noun_phrases2():
            yield determiner + " " +  noun_phrase
    for noun_phrase in noun_phrases2():
        yield noun_phrase

def sentences():
    for noun_phrase in noun_phrases():
        for verb_phrase in verb_phrases():
            yield noun_phrase + " " + verb_phrase

def main():
    tested_sentence = "a boy sings"
    for sentence in sentences():
        if tested_sentence == sentence:
            print("True")
            quit()
    print(False)

if __name__ == "__main__":
    main()
