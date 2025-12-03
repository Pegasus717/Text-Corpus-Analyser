import argparse

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

