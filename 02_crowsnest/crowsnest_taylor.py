#!/usr/bin/env python3
"""
Author : Taylor Stephens <stephens.taylora@gmail.com>
Date   : 2021-06-10
Purpose: Show off my baby python skills
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='word',
                        help='A word')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.positional
    char = word[0].lower()
    article = "an" if char in "aeiou" else "a"
    f'Ahoy, Captain, {article} {word} off the larboard bow!'

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
