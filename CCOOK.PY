n=int(input())
for i in range(n):
  s=list(map(int,input().split()))
  x=0
  x=s[0]+s[1]+s[2]+s[3]+s[4]
  if(x==0): print("Beginner")
  elif(x==1): print("Junior Developer")
  elif(x==2): print("Middle Developer")
  elif(x==3): print("Senior Developer")
  elif(x==4): print("Hacker")
  elif(x==5): print("Jeff Dean") 
