class myQueue:
    def __init__(self,n):
        self.queue=[]
        self.front=0
        self.rear=-1
    def isEmpty(self):
        if self.rear==-1:
            print("queue empty")
    def isFull(self):
        if self.rear==n-1:
            print("queue full")
    def enqueue(self,x):
        self.rear+=1
        self.queue.append(x)
    def dequeue(self):
        if self.front>self.rear:
            print("queue empty")
        else:
            self.front+=1
n=int(input())            
q=myQueue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()