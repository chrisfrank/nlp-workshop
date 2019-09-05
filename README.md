# Python NLP Workshop

Let's learn the basics of Natural Language Processing in Python by building a
tiny search engine.

You'll need Python 3 installed on your machine. This README assumes that your
`python` command runs python3. If your machine is configured differently, try
substituting `python3` throughout.

## Setup
1. Clone this repository:
    ```
    git clone https://github.com/chrisfrank/nlp-workshop.git
    ```
2. Install the required libraries.

    If you're familiar with `venv`, feel free to create a virtual environment and
    source it first. If not, forget I mentioned it.

    ```
    pip install -r requirements.txt
    ```


3. Make sure it works:
    ```
    python -m tokenizer -h
    ```
    If this command produces an error message, ask for help!


## Tokenizing
> Breaking unstructured text into meaningful units
```
python -m tokenizer "This text will be tokenized naively. How might we improve the results?"
```

## Stemming
> Transforming word tokens into ungrammatical root forms

```
python -m stemmer "Let's try to stem this text and see what happens."
```

## Lemmatizing
> Transforming word tokens into grammatical root forms
```
python -m lemmatizer "Let's try to lemmatize this text and see what happens."
```

## Searching
```
python -m search "brexit"
```

## Writing a better search
```
python -m bettersearch "brexit"
```
