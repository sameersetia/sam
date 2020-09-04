import math
# H=10
H=int(input())
# A,B,C,D=[5,5,5,5]
A,B,C,D=[int(i) for i in input().split()]
# VA,VB,VC,VD=[1,2,1,2]
VA,VB,VC,VD=[int(i) for i in input().split()]
# UDa,UDb,UDc,UDd=['D','U','U','D']
UDa,UDb,UDc,UDd=[i for i in input().split()]
Va=VA*(1 if UDa=='U' else -1)
Vb=VB*(1 if UDb=='U' else -1)
Vc=VC*(1 if UDc=='U' else -1)
Vd=VD*(1 if UDd=='U' else -1)
def area(x,y,z):
    xy=((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)**(1/2)
    yz=((z[0]-y[0])**2 + (z[1]-y[1])**2 + (z[2]-y[2])**2)**(1/2)
    xz=((x[0]-z[0])**2 + (x[1]-z[1])**2 + (x[2]-z[2])**2)**(1/2)
    S=(xy+yz+xz)/2
    ar=abs(int((S)*(S-xy)*(S-yz)*(S-xz)))**(1/2)
    return(ar)

a=[0,0,A]
b=[H,0,B]
c=[H,H,C]
d=[0,H,D]
maxar=[area(a,b,c)+area(a,d,c)]
canAmove=True
canBmove=True
canCmove=True
canDmove=True
Count=3
while canAmove or canBmove or canCmove or canDmove:
    if canAmove:
        A+=Va
        if A>=H or A<=0:
            if A>=H:
                a=[0,0,H]
            if A<=0:
                a=[0,0,0]
            Count-=1
            canAmove=False
        else:
            a=[0,0,A]

    if canBmove:
        B+=Vb
        if B>=H or B<=0:
            if B>=H:
                b=[H,0,H]
            if B<=0:
                b=[H,0,0]
            Count-=1
            canBmove=False
        else:
            b=[H,0,B]
    if canCmove:
        C+=Vc
        if C>=H or C<0:
            if C>=H:
                c=[H,H,H]
            if C<=0:
                C=[H,H,0]
            Count-=1
            canCmove=False
        else:
            c=[H,H,C]
            
    if canDmove:
        D+=Vd
        if D>=H or D<=0:
            if D>=H:
                d=[0,H,H]
            if D<=0:
                d=[0,H,0]
            Count-=1
            canDmove=False
        else:
            d=[0,H,D]
    arabc=(area(a,b,c))
    aradc=(area(a,d,c))
    maxar.append((arabc+aradc))
        
print("{0} {1}".format(int(4*(max(maxar)**2)),int(4*(min(maxar)**2))))
