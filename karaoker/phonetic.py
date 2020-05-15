import phonetics
import unidecode
import collections
import itertools
import editdistance


def get_words(txt: str):
    for word in txt.split():
        word = unidecode.unidecode(word.strip(" \r\n\t!,?.")).lower()
        w = (word, phonetics.dmetaphone(word))
        yield w


def get_phrases(txt: str, max_len: int):
    for line in txt.split("\n"):
        buffers = (collections.deque(maxlen=max_len),
                   collections.deque(maxlen=max_len))
        for (w, l) in get_words(line):
            (wb, lb) = buffers
            wb.append(w)
            lb.append(l)
            if len(wb) == max_len:
                yield (line, tuple(itertools.chain(*lb)))
    yield (line, tuple(itertools.chain(*lb)))


def make_model(text: str, max_len: int):
    return (max_len, set(get_phrases(text, max_len)))


def find_best_match(text: str, model):
    (max_len, phrases) = model
    results = list()
    for (phrase, l1) in get_phrases(text, max_len):
        for p2 in phrases:
            (o_p, l2) = p2
            d = editdistance.distance(l1, l2)
            results.append((d * (1 + abs(len(l2) - len(l2))), o_p))
    results.sort(reverse=False)
    return results[0]


if __name__ == "__main__":
    lines = open("lyrics.txt").read()
    model = make_model(lines, 8)
    print(model)
    (score, phrase) = find_best_match("those foolish things", model)
    print(phrase)
