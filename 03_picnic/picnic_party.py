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
                        nargs = '+', 
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
    num = len(item)

    if args.sorted:
        item.sort()

    bringing = " "
    if num == 1:
        bringing = item[0]
    elif num < 3:
        bringing = ' and '.join(item)
    else:
        item[-1] = 'and ' + item[-1]
        bringing = ', '.join(item)


    print(f'You are bringing {bringing}.')
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
