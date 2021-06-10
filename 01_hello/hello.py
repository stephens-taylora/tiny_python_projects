#!/usr/bin/env python3
"""
Author: Taylor Stephens <stephens.taylora@gmail.com>
# Purpose: Say Hello
"""
#----------------------------------------------------------------------
import argparse
def get_args():
    """Get the command-line argument"""
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument("-n", "--name", metavar= "name",
                        default= "World", help="Name to greet")
    args = parser.parse_args()
    return parser.parse_args()
#-----------------------------------------------------------------------
def main():
    """To party lol"""
    args = get_args ()
    print("Hello, " + args.name + "!")
#-----------------------------------------------------------------------
if __name__ == "__main__":
    main()