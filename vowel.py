def checkVowel(s):
    if s=='aeiou' or s=='AEIOU':
        print("Vowel")
    else:
        print("Consonant")
s=input()
print(checkVowel(s))