
def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    num=0
    original=x
    while x!=0:
        digit=x%10
        num=num*10+digit
        x=x//10
    return num==original
x=int(input())
print(isPalindrome(x))