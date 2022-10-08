def solution(A):
    B=A.copy()
    B.sort()
    c=1
    l=0
    n=0

    for i in range (1,len(B)):
        if(B[i]!=B[i-1]):
            c=1
        else:
            c+=1
        if c>len(B)/2:
            l=B[i]
            break
        for i in range(0,len(A)):
            if A[i]==1:
                n+=1

    EqL=0
    c=0

    for i in range (0,len(A)):
        if A[i]==1:
            c+=1
        if (i+1>2*c and len(A)-i-1<2*(n-c)):
            EqL+=1

        return EqL