def isCamelCase(s):
    count=0
    for ch in s:
        if ch.isupper():
            count+=1
    return count
s=input()
print(isCamelCase(s))