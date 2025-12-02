import re 

def normalize_word(w: str) -> str:
    #Normalize word by converting to lowercase and removing accents using regex.
    normalized = re.sub(r'[^\x00-\x7F]+', '', w.lower())
    return normalized if normalized else w.lower()

