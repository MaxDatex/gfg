'''
Given a string s check if it is "Panagram" or not.

    A "Panagram" is a sentence containing every letter in the English Alphabet.

'''


import string

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        alphabeth = set(string.ascii_lowercase)
        return set(s.lower()) >= alphabeth
