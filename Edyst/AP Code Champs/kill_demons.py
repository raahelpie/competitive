"""
This question was the 3rd question in AP CodeChamps Round 2

Do you remember Neville from Harry Potter? Not everyone does.

To be remembered, Neville has to destroy all the demons. Each demon has health and latent energy, and the latent
energy is released when the demon is destroyed, this latent energy reduces the next demon's health.

A demon is destroyed when its health is <= 0

Find the minimum energy required to kill all the demons.

Input format:
First line contains a single integer t denoting the number of test cases
The description of t test cases follow

First line of each test case has a single integer n denoting the number of demons
Then n lines follow each having two integers "a" and "b" where ai is the health of ith demon, and bi is the le of ith demon

Output a single integer that denotes the minimum energy required to destroy all demons
"""

'''
EXPLANATION:


'''


t = int(input())


def answer():
    n = int(input())
    k = n
    omg = []
    while k:
        a, b = map(int, input().split())
        omg.append([a, b])
        k -= 1
    i = 0
    extra = omg[0][0]
    k = extra
    mini = 10**100
    idx = i
    if omg[i][1] >= omg[i+1][0]:
        idx += 1
    else:
        extra += (omg[i+1][0] - omg[i][1])
        idx += 1
    while idx != i:
        if idx == n - 1:
            idx = -1
        if omg[idx][1] >= omg[idx+1][0]:
            idx += 1
        else:
            extra += (omg[idx+1][0] - omg[idx][1])
            idx += 1
    mini = min(mini, extra)
    for i in range(1, n):
        mini = min(mini, extra - k + omg[i][0])


while t:
    print(answer())
    t -= 1