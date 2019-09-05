from nlp import nlp

def lemmatize(text):
    tokens = nlp(text)
    return [
        token.lemma_.lower()
        for token in tokens
        if token.is_alpha and not token.pos_ == "PRON"
    ]

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='Text to lemmatize')
    args = parser.parse_args()

    text = args.text
    lemmas = lemmatize(text)
    [print(lemma) for lemma in lemmas]
