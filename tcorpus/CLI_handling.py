import argparse
import logging
from pathlib import Path
from datetime import datetime
from .main_logic import (
    extract_words,
    extract_alphanumeric_tokens,
    find_palindromes,
    find_anagrams,
    find_frequencies,
    find_mask_matches,
    find_emails,
    find_phone_numbers,
)



def _resolve_input_text(input_value: str, is_text: bool = False) -> str:
    if is_text:
        logging.info("Using provided text input.")
        return input_value
    
    if not input_value:
        raise ValueError("No input provided. Use --text to provide text directly or specify a file path.")
    
    path = Path(input_value)
    if path.exists() and path.is_file():
        logging.info(f"Reading from file: {input_value}")
        return read_text_file(path)
    
    logging.info("Treating input as direct text.")
    return input_value
def _build_stopwords(cli_stopwords, config_path):
    """Combine stopwords from config and CLI."""
    combined = set(load_config_stopwords(config_path))
    if cli_stopwords:
        combined.update(w.lower() for w in cli_stopwords)
    return combined
def process(
    mode,
    input_value,
    output_path,
    mask=None,
    target_words=None,
    phone_digits=None,
    cli_stopwords=None,
    starts_with=None,
    config_path="config.ini",
    is_text=False,
    min_length=None,
    max_length=None,
    exact_length=None,
    contains=None,
    print_words: bool = False,
):
    text = _resolve_input_text(input_value, is_text=is_text)
    stopwords = _build_stopwords(cli_stopwords, config_path)
    starts_with_char = starts_with.lower()[0] if starts_with else None
    words = extract_words(text, stopwords=stopwords or None, starts_with=starts_with_char)
    result = {}



def build_parser():
    parser = argparse.ArgumentParser(prog="WordTools",
                                     description="Toolkit for words, masks, emails, phone numbers",
                                     formatter_class=argparse.RawTextHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def add_input_options(p):
        p.add_argument("input", nargs="?", help="Input file path (optional if using --text)")
        p.add_argument("-t", "--text", dest="input_text", help="Provide text directly instead of file path")
    
    def add_word_filters(p):
        p.add_argument("--stopwords", nargs="+", help="Stopwords to ignore (in addition to config.ini)")
        p.add_argument("--starts-with", help="Keep only words that start with this letter")
        p.add_argument("--config", default="config.ini", help="Path to config file for stopwords")
        p.add_argument(
            "-pw","--print-words",
            action="store_true",
            help="Print filtered words (after stopword/starts-with filters) to the terminal",
        )
    p1 = sub.add_parser("palindrome")
    add_input_options(p1)
    p1.add_argument("output")
    add_word_filters(p1)
    
    p2 = sub.add_parser("anagram")
    add_input_options(p2)
    p2.add_argument("output")
    add_word_filters(p2)
    
    p3 = sub.add_parser("freq")
    add_input_options(p3)
    p3.add_argument("output")
    p3.add_argument("-w", "--words", nargs="+", help="Words to count, 'all' for all")
    add_word_filters(p3)
    
    p4 = sub.add_parser("all", help="Run all analyses: palindromes, anagrams, frequencies, emails, phone numbers")
    add_input_options(p4)
    p4.add_argument("output")
    p4.add_argument("-w", "--words", nargs="+", help="Words to count, 'all' for all")
    p4.add_argument("-d", "--digits", type=int, default=10, help="Number of digits for phone numbers")
    add_word_filters(p4)

    p5 = sub.add_parser("mask", help="Find words matching pattern")
    p5.add_argument("mask", help="Pattern: 'a*d' (wildcard), 'ram+' (starts with), '+ing' (ends with), '+ram+' (contains)")
    add_input_options(p5)
    p5.add_argument("output")
    p5.add_argument("--min-length", type=int, help="Minimum word length")
    p5.add_argument("--max-length", type=int, help="Maximum word length")
    p5.add_argument("--length", type=int, dest="exact_length", help="Exact word length")
    p5.add_argument("--contains", help="Word must contain this substring")
    add_word_filters(p5)

    p6 = sub.add_parser("email", help="Extract emails")
    add_input_options(p6)
    p6.add_argument("output")

    p7 = sub.add_parser("phone", help="Extract phone numbers")
    add_input_options(p7)
    p7.add_argument("output")
    p7.add_argument("-d", "--digits", type=int, default=10, help="Number of digits")

    return parser
