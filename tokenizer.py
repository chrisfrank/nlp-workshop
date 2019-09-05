from nlp import nlp

def tokenize_naively(text):
    return text.split(' ')

def tokenize_magically(text):
    return [tok.text for tok in nlp(text)]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='Text to tokenize')
    parser.add_argument('-a', '--algorithm', help='use "naive" or "magic"')
    args = parser.parse_args()

    ALGORITHMS = {
        'naive': tokenize_naively,
        'magic': tokenize_magically,
    }

    tokenize = ALGORITHMS.get(args.algorithm, ALGORITHMS['naive'])
    text = args.text
    print(tokenize(text))
