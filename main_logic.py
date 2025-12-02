import re 

def normalize_word(w: str) -> str:
    #Normalize word by converting to lowercase and removing accents using regex.
    normalized = re.sub(r'[^\x00-\x7F]+', '', w.lower())
    return normalized if normalized else w.lower()

def extract_words(text: str, stopwords=None, starts_with=None):
    words = re.findall(r"[a-zA-Z]+", text)
    normalized = [normalize_word(w) for w in words]
    stopword_set = {normalize_word(w) for w in stopwords} if stopwords else set()
    starts_with = starts_with.lower()[0] if starts_with else None
    filtered = []
    for word in normalized:
        if stopword_set and word in stopword_set:
            continue
        if starts_with and not word.startswith(starts_with):
            continue
        filtered.append(word)
    return filtered
