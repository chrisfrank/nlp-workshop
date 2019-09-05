from pathlib import Path

def load_articles():
    filepaths = Path("articles").glob('*.md')
    articles = []
    for filepath in filepaths:
        article = {
            'title': filepath.stem,
            'body': filepath.read_text(),
        }
        articles.append(article)
    return articles

ARTICLES = load_articles()
