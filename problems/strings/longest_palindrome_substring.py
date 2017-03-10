"""
Longest Palindrome in a String.

Given a string S, find the longest palindromic substring in S.

Substring of string S:
S[ i . . . . j ] where 0 <= i<= j < len(S)

Palindrome string:
A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
Incase of conflict, return the substring which occurs first ( with the least starting index ).

Input:
The first line of input consists number of the test cases. The following T lines consist of a string each.

Output:
In each separate line print the longest palindrome of the string given in the respective test case.

Constraints:
1 <=  <= 70
1<= st <= 100

Example:
Input:
1
aaaabbaa

Output:
aabbaa

From: http://www.practice.geeksforgeeks.org/problem-page.php?pid=392
"""


def longest_palindrome_substring(s):
    count = len(s)
    table = {i: {j: i == j for j in range(0, count)} for i in range(0, count)}
    max_len = 0
    max_i = 0
    max_j = 1

    for i in range(0, count - 1):
        if s[i] == s[i + 1]:
            if max_len == 0:
                max_len = 1
                max_i = i
                max_j = i + 2
            table[i][i + 1] = True

    for palindrome_len in range(3, count + 1):
        for i in range(0, count - palindrome_len + 1):
            j = i + palindrome_len - 1
            if table[i + 1][j - 1] and s[i] == s[j]:
                table[i][j] = True
                if j - i > max_len:
                    max_len = j - i
                    max_i = i
                    max_j = j + 1

    return s[max_i:max_j]
