#! /usr/bin/env python

# hitjim@gmail.com
# palindrome permutation checker
# http://www.upfrontwichita.com/challenges/2
#
# usage guide:
# use it

import sys
import argparse
import collections 

parser = argparse.ArgumentParser(description='Enter string to see if it\'s a palindrome.')
parser.add_argument('string', help="string to be tested for palindromedness..ishness")
args = parser.parse_args()

arg = args.string

char_counter = collections.Counter()

# parse input string, find alphanumeric characters, make 
# lowercase if necessary, and add to counter dict object
for i in arg:
    if i.isalnum():
        if i.isupper():    
            i=i.lower();
        char_counter[i] += 1

odds_tally = 0

# parse counter object by element, if > 1 character with
# an odd count, not a palindrome
for i in char_counter:
    if odds_tally <= 1:
        if char_counter[i]%2 != 0:
            odds_tally += 1
    else:
        break

if odds_tally <=1:
    print "CAN BE PERMUTATED INTO A PALINDROME"
else:
    print "CAN NOT BE PERMUTATED INTO A PALINDROME"
