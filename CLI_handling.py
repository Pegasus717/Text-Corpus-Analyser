import argparse

def build_parser():
    parser = argparse.ArgumentParser(prog="WordTools",
                                     description="Toolkit for words, masks, emails, phone numbers",
                                     formatter_class=argparse.RawTextHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    