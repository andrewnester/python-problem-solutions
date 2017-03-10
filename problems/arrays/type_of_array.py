"""
Type of array

Given an array having no dublicates, which can be of 4 types
1.  Ascending
2.  Descending
3.  Descending Rotated
4.  Ascending Rotated
Your task is to print which type of array it is and the maximum
element of that array.

Input :  A[] = { 2, 1, 5, 4, 3}
Output : Descending rotated with maximum element 5

Input :  A[] = { 3, 4, 5, 1, 2}
Output : Ascending rotated with maximum element 5

Input:
The first line of input contains an integer T denoting the no test cases.
Then T test caes follow. The first line of input contains an integer n
denoting the size of the array. Then in the next line are N space separated
values of the array.

Output:
For each test case print the largest element in the array and and integer x
denoting the type of the array.

Constraints:
1<=T<=100
4<=n<=100
1<=A[]<=1000

Example:
Input:
2
5
2 1 5 4 3
5
3 4 5 1 2

Output:
5 3
5 4

From: http://www.practice.geeksforgeeks.org/problem-page.php?pid=1687

"""

ASCENDING = 1
DESCENDING = 2
DESCENDING_ROTATED = 3
ASCENDING_ROTATED = 4


def get_type_of_array_and_max(arr):
    i = 1
    while i < len(arr) - 1:
        a1 = arr[i - 1] - arr[i]
        a2 = arr[i] - arr[i + 1]
        print (a1, a2)
        if a1 > 0 > a2:
            return (arr[i + 1] if (a1 + a2) < 0 else
                    arr[i - 1],
                    DESCENDING_ROTATED if (a1 + a2) < 0 else ASCENDING_ROTATED)
        if a1 < 0 < a2:
            return (arr[i],
                    DESCENDING_ROTATED if (a1 + a2) < 0 else ASCENDING_ROTATED)
        i += 1

    # ascending, max at the end
    if arr[0] - arr[1] < 0:
        return arr[len(arr) - 1], ASCENDING

    return arr[0], DESCENDING
