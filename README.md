# Maximum Possible Substrings

This is my solution in Python 3.8+ for the following problem:

Create a small repo with a solution on Python for a educational problem:
`#!/usr/bin/perl`
Given a string of latin characters. Split it on maximum possible substrings in a way that each character is present in not more then one substring. Return a vector of sizes of these substrings. examples:
- in: ababababcdddfh out: [8, 1, 3, 1, 1] abababab c ddd f h
- in: aaabbbab out: [8] could not split
- in: acbad out: [4, 1] acba d
