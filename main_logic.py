import re 

def normalize_word(w: str) -> str:
    #Normalize word by converting to lowercase and removing accents using regex.
    normalized = re.sub(r'[^\x00-\x7F]+', '', w.lower())
    return normalized if normalized else w.lower()

def extract_words(text: str, stopwords=None, starts_with=None):
    words = re.findall(r"[a-zA-ZÀ-ÖØ-öø-ÿ]+", text)
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
def extract_alphanumeric_tokens(text: str, stopwords=None, starts_with=None):
    tokens = re.findall(r"[a-zA-Z0-9À-ÖØ-öø-ÿ]+", text)
    normalized = []
    for token in tokens:
        normalized_token = re.sub(r'[^\x00-\x7F]+', '', token.lower())
        if normalized_token:
            normalized.append(normalized_token)
    
    stopword_set = set()
    if stopwords:
        for w in stopwords:
            normalized_stopword = re.sub(r'[^\x00-\x7F]+', '', w.lower())
            if normalized_stopword:
              stopword_set.add(normalized_stopword)
    
    starts_with_char = None
    if starts_with:
        if starts_with[0].isdigit():
            starts_with_char = starts_with[0]
        else:
            starts_with_char = starts_with.lower()[0]
    
    
    filtered = []
    for token in normalized:
        if stopword_set and token in stopword_set:
            continue
        if starts_with_char and not token.startswith(starts_with_char):
            continue
        filtered.append(token)
    return filtered

