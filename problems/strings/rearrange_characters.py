"""
Given a string with repeated characters, task is to rearrange characters in
a string such that no two adjacent characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.


Input:
The first line of input contains an integer T denoting the number of
test cases. Then T test cases follow. Each test case contains a single line
containing a string of lowercase english alphabets.

Output:
For each test case in a new line print 1 if the generated sting doesn't
contains any same adjacent characters, else if no such string is possible to
be made print 0.

Constraints:
1<=T<=100
1<=length of string<=600

Example:
Input:
3
geeksforgeeks
bbbabaaacd
bbbbb

Output:
1
1
0

From: http://practice.geeksforgeeks.org/problem-page.php?pid=1701
"""

from collections import Counter


def is_possible_to_rearrange(input_string):
    counter = Counter()
    for c in input_string:
        counter[c] += 1

    char, amount = counter.most_common(1)[0]
    return amount * 2 <= len(input_string) - 1
