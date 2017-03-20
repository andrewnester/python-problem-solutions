"""
Check if string is rotated by two places.

Given two strings, the task is to find if a string ('a') can be obtained by
rotating another string ('b') by two places.
Examples:

Input : a = "amazon"
        b = "azonam"  // rotated anti-clockwise
Output : 1

Input : a = "amazon"
        b = "onamaz"  // rotated clockwise
Output : 1


Input:
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow. In the next two line are two string a and b.

Output:
For each test case in a new line print 1 if the string 'a' can be obtained by
rotating string 'b' by two places else print 0.

Constraints:
1<=T<=50
1<=length of a, b <100

Example:
Input:
2
amazon
azonam
geeksforgeeks
geeksgeeksfor
Output:
1
0

From here: http://www.practice.geeksforgeeks.org/problem-page.php?pid=1707
"""


def is_rotated_by_two(a, b):
    right_rotated = _rotate_right(b)
    left_rotated = _rotate_left(b)

    if a == right_rotated or a == left_rotated:
        return 1

    return 0


def _rotate_left(s):
    return s[2:] + s[:2]


def _rotate_right(s):
    return s[-2:] + s[:-2]
