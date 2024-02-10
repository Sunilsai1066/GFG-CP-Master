def alternateArray(Lis, N):
    DupLis = [0]*N
    PosInd, NegInd = 0, N-1
    for num in Lis:
        if(num >= 0):
            DupLis[PosInd] = num
            PosInd += 1
        else:
            DupLis[NegInd] = num
            NegInd -= 1
    ResLis = []
    #print(DupLis, PosInd, NegInd)
    if(PosInd == N):
        return DupLis
    elif(NegInd == -1):
        return reversed(DupLis)
    Flag = 1
    PosFin, NegFin = 0, N-1
    for i in range(N):
        if(Flag == 1 and PosFin < PosInd):
            ResLis.append(DupLis[PosFin])
            PosFin += 1
            if(NegFin > NegInd):
                Flag = 0
        elif(NegFin > NegInd):
            ResLis.append(DupLis[NegFin])
            NegFin -= 1
            if(PosFin < PosInd):
                Flag = 1
    return ResLis
    
    
    
    
    

T = int(input())
for C in range(T):
    N = int(input())
    Lis = list(map(int, input().strip().split()))
    print(*alternateArray(Lis, N))
