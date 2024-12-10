A Python program to solve Scrabble-like word puzzles by finding all valid words that can be formed from a given set of letters, including blanks (_) as wildcards. The program leverages an efficient Trie data structure for fast dictionary lookups and includes optimizations like early termination and dynamic wildcard substitution.

Features:

Dictionary Integration: Uses a Trie for efficient word validation and prefix checking.
Wildcard Handling: Supports blank tiles (_), substituting them with any letter (A–Z).
Word Scoring: Calculates Scrabble scores for all valid words and sorts them by score and alphabetically.
Optimized Performance: Early termination of invalid branches to save computational resources.
