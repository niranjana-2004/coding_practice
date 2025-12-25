def armstrong(n):
    temp=n
    flag=0
    sum=0
    k=len(str(n))

    while n>0:
        digit=n%10
        sum+=digit**k
        n//=10
    if sum==temp:
        print("armstrong")
    else:
        print("nor armstrong")
n=int(input())
armstrong(n)