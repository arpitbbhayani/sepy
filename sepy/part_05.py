from nltk.stem import PorterStemmer 
   
ps = PorterStemmer() 
m = {}


def normalize(word):
    """Given the word `word`, return normalized version of it.

    Ex: Use Porter stemmer to stem the word to its root form
    """
    if word not in m:
        m[word] = ps.stem(word)

    return m[word]
