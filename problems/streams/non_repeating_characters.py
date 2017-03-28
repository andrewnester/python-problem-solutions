"""
Given an input stream of n characters consisting only of small case alphabets the task is to find the first non repeating character each time a character is inserted to the stream.

Example

Flow in stream : a, a, b, c
a goes to stream : 1st non repeating element a (a)
a goes to stream : no non repeating element -1 (5, 15)
b goes to stream : 1st non repeating element is b (a, a, b)
c goes to stream : 1st non repeating element is b (a, a, b, c)

Input:
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow. Each test case contains an integer N denoting
the size of the stream. Then in the next line are x characters
which are inserted to the stream.

Output:
For each test case in a new line print the first non repeating elements
separated by spaces present in the stream at every instinct when a character
is added to the stream, if no such element is present print -1.

Constraints:
1<=T<=200
1<=N<=500

Example:
Input:
2
4
a a b c
3
a a c
Output:
a -1 b b
a -1 c

From: http://practice.geeksforgeeks.org/problem-page.php?pid=1736
"""


def get_non_repeating_characters(stream):
    letters_count = {}
    possible_non_repeated = []
    current = '-1'
    non_repeated = []

    for c in stream:
        count = letters_count.setdefault(c, 0)
        count += 1
        letters_count[c] = count

        if current == c:
            current = get_next_possible(possible_non_repeated, letters_count)
            non_repeated.append(current)
            continue

        if letters_count[c] > 1:
            non_repeated.append(current)
            continue

        if current == '-1':
            current = c
        else:
            possible_non_repeated.append(c)

        non_repeated.append(current)

    return non_repeated


def get_next_possible(possible, taken):
    while len(possible) > 0:
        p = possible.pop(0)
        if p not in taken or taken[p] == 1:
            return p

    return '-1'
