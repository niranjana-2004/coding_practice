#taking count of factors
'''n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print('prime')
else:
    print('not prime')'''

#method 2
'''n=int(input())
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
        break
if prime:
    print('prime')
else:
    print('not prime')'''

#method 3 
n=int(input())
prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        prime=False
        break
if prime:
    print('prime')
else:
    print('not prime')