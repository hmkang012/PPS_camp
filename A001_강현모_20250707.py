def findContentChildren(self, g, s):
    g.sort()
    s.sort()

    number = 0
    i = 0
    j = 0

    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            i += 1
            j += 1
            number += 1
        else:
            i += 1
            
    return number
