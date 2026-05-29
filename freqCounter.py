s=input()
freq={}
max_ch=""
max_count=0
for ch in s:
    freq[ch]=freq.get(ch,0)+1
    if freq[ch]>max_count:
        max_count=freq[ch]
        max_ch=ch
print(freq)
print("Character ",max_ch,"occurred the most ","with ",max_count,"times")