def Sum(n):
    sum=0
    while n>0:
        sum+=(n%10)
        n=n//10
    return sum
def palindromeSum(n):
    d=1
    while(n//d>=10):
        d*=10
    while(n!=0):
        l=n//d
        t=n%10
        if(l!=t):
            return False
        n=(n%d)//10
        d=d//100
    return True
def isDigitSumPalindrome(n) : 
    sum = Sum(n); 
    if (palindromeSum(sum)) :
        return True; 
    return False; 

if __name__ == "__main__" : 

    n = 56; 

    if (isDigitSumPalindrome(n)) :
        print("true"); 
    else :
        print("false");