"""
Find all four sum numbers

Given an array A of size N,
find all combination of four elements in the array whose sum is equal
to a given value K.
For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and K = 23,
one of the quadruple is "3 5 7 8" (3 + 5 + 7 + 8 = 23).

Input:
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow. Each test case contains two lines.
The first line of input contains two integers N and K.
Then in the next line are N space separated values of the array.

Output:
For each test case in a new line print all the quadruples present
in the array separated by space which sums up to value of K.
Each quadruple is unique which are separated by a delimeter "$" and
are in increasing order.

Constraints:
1<=T<=100 1<=N<=100 -1000<=K<=1000 -100<=A[]<=100

"""

from itertools import permutations


def get_sum_of_four(arr, K):
    sums_of_two = {}
    count = len(arr)
    for i in range(0, count):
        for j in range(i + 1, count):
            sums_of_two.setdefault(arr[i] + arr[j], []).append(
                (i, j))

    possible_sums = set()
    for s in sums_of_two.keys():
        if s * 2 >= K:
            continue
        if K - s in sums_of_two:
            first_pairs = sums_of_two[s]
            second_pairs = sums_of_two[K - s]
            for a, b in first_pairs:
                for c, d in second_pairs:
                    if a != c and a != d and b != c and b != d:
                        need_to_add = True
                        for p in permutations([a, b, c, d]):
                            if p in possible_sums:
                                need_to_add = False
                                break
                        if need_to_add:
                            possible_sums.add((a, b, c, d))

    return [(arr[p[0]], arr[p[1]], arr[p[2]], arr[p[3]]) for p in
            possible_sums]
