t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split(" ")))
	o=0
	for i in a:
		if(i%2!=0):
			o+=1
	if(o%2==0 or n==1):
		print(1)
	else:
		print(2)
