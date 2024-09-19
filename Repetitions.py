n=input().upper()
len_n=len(n)
count=0
maxi=0
for i in range(len_n-1):
	if n[i]==n[i+1]:
		count+=1
		if maxi<=count:
			maxi=count
	elif n[i]!=n[i+1]:
			count=0
print(maxi+1)
  
