t1,t2=input().split()
if int(t1)%5 != 0 or (float(t1)+0.50) > float(t2) :
    print(t2)
else:
    print( float(float(t2)-int(t1)-0.50) )
