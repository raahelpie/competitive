t = int(input())
def answer():
    A, k, H = map(int, input().split())
    calendar = input()
    l = len(calendar)
    i = 0
    idx = 0
    haha = {}
    gecount = 0
    ecount = 0
    while i < l:
        if calendar[i] == "P":
            idx += 1
            i += 1
            while i < l and calendar[i] == "E":
                ecount += 1
                gecount += 1
                i += 1
            haha[idx] = ecount
            ecount = 0
        elif calendar[i] == "E":
            i += 1
    def score(A):
        ability = A
        score = 0
        for key in haha:
            ability *= k
            score += ability*haha[key]
        return score
    kiki = score(A)
    if kiki < H:
        return 0
    if A*gecount >= H:
        return -1
    else:
        swaps = 0
        difference = kiki - H
        while difference >= 0 and idx >= 1:
            if haha[idx] > 0:
                difference -= (A*(k**idx)) - (A*(k**(idx-1)))
                swaps += 1
                try:
                    haha[idx] -= 1
                    haha[idx-1] += 1
                except KeyError:
                    haha[idx] -= 1
            else:
                idx -= 1
        if idx == 0:
            return -1
        return swaps
while t:
    print(answer())
    t -= 1