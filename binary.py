def binaryString(s):
    for ch in s:
        if ch!='1' and ch!='0':
            return False
    return True
print(binaryString("1001"))