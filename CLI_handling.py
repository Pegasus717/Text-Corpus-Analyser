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
    

    

