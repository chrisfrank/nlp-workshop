from articles import ARTICLES

def search(query):
    print("This search algorithm hasn't been implemented yet.")
    results = []
    return results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='what you want to search for')
    args = parser.parse_args()

    results = search(args.query)
    print("Results:", len(results))
    for article in results:
        print(article['title'], '-', article['body'].split('\n', 1)[0])
