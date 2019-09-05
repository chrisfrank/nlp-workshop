from porter2stemmer import Porter2Stemmer
from tokenizer import tokenize_magically

stemmer = Porter2Stemmer()

def stem(token):
    return stemmer.stem(token).lower()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='Text to stem')
    args = parser.parse_args()

    text = args.text

    # This will work on a single word, but not a sentence:
    print(stem(text))

    # To stem a sentence, we need to tokenize it first.
    # tokens = tokenize_magically(text)
    # for token in tokens:
        # print(stem(token))
