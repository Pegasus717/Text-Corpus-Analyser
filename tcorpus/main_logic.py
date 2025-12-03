import re 

def normalize_word(w: str) -> str:
    normalized = re.sub(r'[^\x00-\x7F]+', '', w.lower())
    return normalized if normalized else w.lower()

def extract_words(text: str, stopwords=None, starts_with=None):
    words = re.findall(r"[a-zA-ZÀ-ÖØ-öø-ÿ]+", text)
    normalized = [normalize_word(w) for w in words]

    stopword_set = {normalize_word(w) for w in stopwords} if stopwords else set()

    starts_with_char = starts_with.lower()[0] if starts_with else None

    filtered = []
    for word in normalized:
        if word in stopword_set:
            continue
        if starts_with_char and not word.startswith(starts_with_char):
            continue
        filtered.append(word)

    return filtered

def extract_alphanumeric_tokens(text: str, stopwords=None, starts_with=None):

    tokens = re.findall(r"[a-zA-Z0-9À-ÖØ-öø-ÿ]+", text)

    normalized = [normalize_word(t) for t in tokens]

    stopword_set = {normalize_word(w) for w in stopwords} if stopwords else set()
    starts_with_char = starts_with[0].lower() if starts_with else None

    filtered = []
    for token in normalized:
        if token in stopword_set:
            continue
        if starts_with_char and not token.startswith(starts_with_char):
            continue
        filtered.append(token)

    return filtered

def find_palindromes(words):
    return sorted({w for w in words if len(w) > 2 and w == w[::-1]})
def find_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, set()).add(w)

    output = [sorted(group) for group in groups.values() if len(group) > 1]

    return sorted(output, key=lambda g: (len(g), g))

def find_frequencies(words, target_words=None):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    if not target_words or "all" in [w.lower() for w in target_words]:
        return dict(sorted(freq.items()))

    target_words = [w.lower() for w in target_words]
    return {w: freq[w] for w in target_words if w in freq}
def find_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return sorted(set(re.findall(pattern, text)))

