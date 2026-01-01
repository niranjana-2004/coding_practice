def cntDistinct(st):
    s = set([])
    for i in range(len(st)):
        s.add(st[i])
    return len(s)
if __name__ == "__main__":
    st = "geeksforgeeks"
    print(cntDistinct(st))