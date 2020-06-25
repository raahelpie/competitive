'''
Chef made N pieces of cakes, numbered them 1 through N and arranged them in a row in this order.
There are K possible types of flavours (numbered 1 through K); for each valid i, the i-th piece of cake has a flavour Ai.

Chef wants to select a contiguous sub-segment of the pieces of cake such that-
there is at least one flavour which does not occur in that subsegment.
Find the maximum possible length of such a subsegment of cakes.

Input:

The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains two integers N and K.
The second line contains N space-separated integers A1,A2,…,AN.


Output:  For each test case, print a single line containing one integer ― the maximum length of a valid subsegment.

Example Input:
2
6 2
1 1 1 2 2 1
5 3
1 1 2 2 1
Example Output:
3
5
'''
t = int(input())


def longest_sub():
    n, k = map(int, input().split())
    flavours = list(map(int, input().split()))
    # seen = set()
    # start = {}
    # end = {}
    # unique = 0
    # maxi = {}
    # for i in range(n):
    #     if flavours[i] not in seen:
    #         start[flavours[i]] = i
    #         end[flavours[i]] = i
    #         seen.add(flavours[i])
    #         unique += 1
    #         maxi[flavours[i]] = -1
    #     else:
    #         maxi[flavours[i]] = max(maxi[flavours[i]], i - end[flavours[i]] - 1)
    #         end[flavours[i]] = i
    # print(start)
    # print(end)
    # if unique < k:
    #     return n
    # else:
    #     gans = 0
    #     for each in seen:
    #         ans = max(start[each], n - 1 - end[each], maxi[each])
    #         gans = max(ans, gans)
    #     return gans
    st = set()
    count = {}
    start, res = 0, 0
    for i in range(n):
        if flavours[i] in st:
            count[flavours[i]] += 1
        else:
            st.add(flavours[i])
            count[flavours[i]] = 1
        if len(st) == k:
            while len(st) == k:
                count[flavours[start]] -= 1
                if count[flavours[start]] == 0:
                    st.remove(flavours[start])
                start += 1
        res = max(res, i - start + 1)
    return res
for i in range(t):
    print(longest_sub())

"""
10 4
1 2 1 2 1 2 4 3 3 1

set = {2: 1, 4: 1, 3: 1}

"""