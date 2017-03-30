"""
Given an input stream of n integers the task is to insert integers to stream
and print the median of the new stream formed by each insertion of x
to the stream.

Example

Flow in stream : 5, 15, 1, 3
5 goes to stream --> median 5 (5)
15 goes to stream --> median 10 (5, 15)
1 goes to stream --> median 5 (5, 15, 1)
3 goes to stream --> median 4 (5, 15, 1, 3)

Input:
The first line of input contains an integer N denoting the no of elements of
the stream. Then the next N lines contains integer x denoting the no
to be inserted to the stream.

Output:
For each element added to the stream print the floor of the new median
in a new line.

Constraints:
1<=N<=10^5+7
1<=x<=10^5+7

Example:
Input:
4
5
15
1
3

Output:
5
10
5
4

From: http://practice.geeksforgeeks.org/problem-page.php?pid=1731
"""


from heapq import heappop, heappush


def heap_balance(heap_1, heap_2):
    if len(heap_1) == len(heap_2):
        return 0
    elif len(heap_1) > len(heap_2):
        return 1
    else:
        return -1


def find_median(stream):
    res = []
    left_heap = []
    right_heap = []
    median = 0

    for num in stream:
        balance = heap_balance(left_heap, right_heap)
        if balance == 1:
            if num < median:
                root = -heappop(left_heap)
                heappush(right_heap, root)
                heappush(left_heap, -num)
            else:
                heappush(right_heap, num)

            median = (-left_heap[0] + right_heap[0]) // 2

        elif balance == -1:
            if num < median:
                heappush(left_heap, -num)
            else:
                root = heappop(right_heap)
                heappush(left_heap, -root)
                heappush(right_heap, num)

            median = (-left_heap[0] + right_heap[0]) // 2
        else:
            if num < median:
                heappush(left_heap, -num)
                median = -left_heap[0]
            else:
                heappush(right_heap, num)
                median = right_heap[0]

        res.append(median)
    return res
