T=int(input())
for i in range(T):
  N = int(input())
  A= list(map(int,input().split()))
#  print(A )
  
  i = 0
  while True :
    j = 1 + i 
    while True :
#      print("i",i)
#      print("j",j)
#      print("N", N)
#      print(A)
      if j >= N-1 or j>len(A):
        break
      sum = A[i]+A[j] 
      if sum % 2 == 0 :
        A.append(sum) 
        A.remove(A[i])
        A.remove(A[j-1])
#        print(A)
        j = 1 + i
      else:
        j+= 1
      
      if len(A) == 1 or  j >= N-1 :
        break;
    if i >= N-1 :
      break
    i += 1

  print(len(A))
