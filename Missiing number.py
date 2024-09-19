n=int(input())
a=n*(n+1)//2 - sum([int(i) for i in input().split()])
# sum of first n number - sum of given number=missing number
print(a)

