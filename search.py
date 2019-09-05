from articles import ARTICLES
from lemmatizer import lemmatize

def run_basic_search(query):
    results = []
    for article in ARTICLES:
        if query in article['body']:
            results.append(article)
    return results

def run_advanced_search(query):
    results = []
    query_lemmas = lemmatize(query)
    for article in ARTICLES:
        article_lemmas = lemmatize(article['title'] + '\n' + article['body'])
        for lemma in article_lemmas:
            if lemma in query_lemmas:
                results.append(article)
                break
    return results

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='what you want to search for')
    parser.add_argument('-a', '--algorithm', help='use "basic" or "advanced"')
    args = parser.parse_args()

    ALGORITHMS = {
        'basic': run_basic_search,
        'advanced': run_advanced_search,
    }


    search = ALGORITHMS.get(args.algorithm, ALGORITHMS['basic'])
    results = search(args.query)

    print("Results:", len(results))
    for article in results:
        print(article['title'], '-', article['body'].split('\n', 1)[0])
