# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

from Exes_and_Ohs import xo

if xo('xo')    == True: print("ok")
if xo('xo0')   == True: print("ok")
if xo('xxxoo') == False: print("ok")

if xo("ooxx")    == True:  print("ok")
if xo("xooxx")   == False: print("ok")
if xo("ooxXm")   == True:  print("ok")
if xo("zpzpzpp") == True:  print("ok")
if xo("zzoo")    == False: print("ok")

