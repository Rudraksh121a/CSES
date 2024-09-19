# even=divide by 2
# odd (multiply by 3)+1

def WA(n):
	if (n & 1):   #odd 
		n=(n*3)+1
		return n
	else:
		n=n//2
		return n


num=int(input())
res=[num]
while (num !=1):
	num=WA(num)
	res.append(num)
	
for i in res:
	print(i,end=" ")

