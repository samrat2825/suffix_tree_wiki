from matplotlib.pyplot import title
import wikipedia
# https://en.wikipedia.org/wiki/Synthetic_diamond


def fetchData(url):
    title = url.split('/')[-1]
    print("\nTitle: {}\n".format(title))
    wiki = wikipedia.page(title)
    text = wiki.content
    return text
