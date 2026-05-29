string=input()
count=0
for ch in string:
    if ch.isalpha() and ch not in 'aeiouAEIOU':
        count+=1
print(count)