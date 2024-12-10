from itertools import permutations
from collections import defaultdict

class TrieNode:
    """A Trie node for storing the dictionary."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """A Trie to efficiently store and search for words."""
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """Check if a word is in the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word in the Trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def score_word(word):
    """Calculate the Scrabble score for a word."""
    LETTER_SCORES = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
        'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
        'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10
    }
    return sum(LETTER_SCORES.get(char, 0) for char in word)

def generate_permutations(letters, blanks, trie, prefix="", results=set()):
    """Recursive function to generate permutations."""
    if prefix and not trie.starts_with(prefix):
        return  # early termination: No word starts with the current prefix
    
    if trie.search(prefix):
        results.add(prefix)  # Add valid word
    
    if not letters and blanks == 0:
        return  # No more letters or blanks to process
    
    # use a letter
    for i, letter in enumerate(letters):
        generate_permutations(letters[:i] + letters[i+1:], blanks, trie, prefix + letter, results)
    
    # using a blank (wildcard)
    if blanks > 0:
        for replacement in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            generate_permutations(letters, blanks - 1, trie, prefix + replacement, results)

def scrabble_solver(letters, dictionary):
    """Solve Scrabble for given letters and a dictionary."""
    # building the Trie
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    

    blanks = letters.count('_')
    available_letters = [l for l in letters if l != '_']

    results = set()
    generate_permutations(available_letters, blanks, trie, results=results)
    

    return sorted(results, key=lambda x: (-score_word(x), x))

letters = ["A", "B", "C", "_", "E"]  # input letters
dictionary = {"ACE", "BA", "CAB", "BE", "CE", "FACE", "BARE", "CARE"}  # example dictionary
valid_words = scrabble_solver(letters, dictionary)
print(valid_words)
