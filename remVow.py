def removeVowel(s):
    v="aeiouAEIOU"
    res=""

    for ch in s:
        if ch not in v:
            res+=ch
    return res
print(removeVowel("niranjana"))