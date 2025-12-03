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

def find_phone_numbers(text, digits=10):
    """Extract phone numbers with minimum digit count."""
    phone_regex = re.compile(
        r"""
        (?<!\d)
        (?:\+?\d{1,3}[\s\-\.]?)?
        (?:\(?\d{2,4}\)?[\s\-\.]?){1,3}
        \d{3,4}
        (?!\d)
        """,
        re.VERBOSE,
    )

    results = set()

    for m in phone_regex.finditer(text):
        raw = m.group().strip()
        only_digits = re.sub(r"\D", "", raw)
        if len(only_digits) >= digits:
            results.add(raw)

    return sorted(results)


def _mask_to_regex(mask: str) -> str:

    mask = mask.strip()

    if mask.endswith('+') and not mask.startswith('+') and '*' not in mask and '?' not in mask:
        # starts with
        base = re.escape(mask[:-1])
        return f"^{base}.*"

    if mask.startswith('+') and not mask.endswith('+') and '*' not in mask and '?' not in mask:
        # ends with
        base = re.escape(mask[1:])
        return f".*{base}$"

    if mask.startswith('+') and mask.endswith('+') and '*' not in mask and '?' not in mask:
        # contains
        base = re.escape(mask[1:-1])
        return f".*{base}.*"

    pattern = []
    for ch in mask:
        if ch == '*':
            pattern.append(".*")
        elif ch == '?':
            pattern.append(".")
        else:
            pattern.append(re.escape(ch))

    return "^" + "".join(pattern) + "$"

def find_mask_matches(words, mask: str,
                      min_length=None, max_length=None,
                      contains=None, exact_length=None):
    regex = re.compile(_mask_to_regex(mask.lower()))

    matches = []
    for word in words:
        w = word.lower()

        if not regex.match(w):
            continue

        if exact_length is not None and len(word) != exact_length:
            continue
        if min_length is not None and len(word) < min_length:
            continue
        if max_length is not None and len(word) > max_length:
            continue
        if contains and contains.lower() not in w:
            continue

        matches.append(word)

    return sorted(set(matches))