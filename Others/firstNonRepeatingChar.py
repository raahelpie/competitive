def fnrc(some):
    nonrepeating = {}
    seen = set()
    for i in range(len(some)):
        if some[i] in seen:
            if some[i] in nonrepeating:
                del nonrepeating[some[i]]
        else:
            nonrepeating[some[i]] = i
            seen.add(some[i])
    for key in nonrepeating:
        return key


print(fnrc("aaabcccdeeef"))