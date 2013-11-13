#! /usr/bin/env python

# hitjim@gmail.com
# palindrome permutation checker
# http://www.upfrontwichita.com/challenges/2
#
# usage guide:
# use it

import sys
import argparse


# Argument parsing
parser = argparse.ArgumentParser(description='Enter string to see if it\'s a palindrome.')
parser.add_argument('string', help="string to be tested for palindromedness..ishness")
args = parser.parse_args()

print args.string
arg = args.string

# Assume single string.  Strings with whitespace need to be in double-quotes
# Test for, and remove whitespace if they exist
# ACTUALLY, wouldn't even need to test for whitespace if we just stripped each string
# regardless of whitespace presence.  You figure strip parses the string anyhow.  Why 
# do it TWICE!?  IDIOT!

arg = arg.replace(" ", "")
print "string w/o whitespace"
print arg

print "convert to lowercase"
arg = arg.lower()
print arg

# Deal with short-circuits first
# If odd
#    If >1 letter which occurs an odd number of times - die, ret false
# If even
#    If >0 letter occurs an odd number of times - die, ret false
# else ret true

print "length of string"
print len(arg)	

if ( len(arg)%2 ) != 0:
	print "string length is odd!!"
else:
	print "string length is even!!"


print "list individual characters within string"
charset = set(arg)
print charset
