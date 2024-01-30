'''
Complete the Insert and Search functions for a Trie Data Structure. 

    Insert: Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
    Search: Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.

'''


class Solution:
    #Function to insert string into TRIE.
    def char_to_index(self, char):
        return ord(char) - ord('a')
    def insert(self, root, key):
        temp = root
        length = len(key)
        
        for i in range(length):
            index = self.char_to_index(key[i])
            if not temp.children[index]:
                temp.children[index] = TrieNode()
            temp = temp.children[index]
            
        temp.isEndOfWord = True
        
            
    
    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        
        temp = root
        length = len(key)
        
        for i in range(length):
            index = self.char_to_index(key[i])
            if not temp.children[index]:
                return 0
            temp = temp.children[index]
        return int(temp.isEndOfWord)
