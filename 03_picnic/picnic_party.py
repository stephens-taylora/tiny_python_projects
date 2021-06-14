#!/usr/bin/env python3
"""
Author : Taylor Stephens <stephens.taylora@gmail.com>
Date   : 2021-06-13
Purpose: Prove I can freaking code
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item', 
                        metavar='str',
                        help='Item(s) to bring')


    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    item = args.item



    print(f'You are bringing {item}!')
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
