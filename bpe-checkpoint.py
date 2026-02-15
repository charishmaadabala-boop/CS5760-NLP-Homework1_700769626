# Mini BPE 
from collections import Counter

corpus = [
    "low","low","low","low","low",
    "lowest","lowest",
    "newer","newer","newer","newer","newer","newer",
    "wider","wider","wider",
    "new","new"
]

corpus = [" ".join(list(w)) + " _" for w in corpus]

def get_bigrams(corpus):
    counts = Counter()
    for word in corpus:
        symbols = word.split()
        for i in range(len(symbols)-1):
            counts[(symbols[i], symbols[i+1])] += 1
    return counts

def merge(corpus, pair):
    bigram = " ".join(pair)
    merged = "".join(pair)
    return [w.replace(bigram, merged) for w in corpus]

for i in range(3):
    pairs = get_bigrams(corpus)
    best = max(pairs, key=pairs.get)
    print(f"Merge {i+1}: {best}")
    corpus = merge(corpus, best)
