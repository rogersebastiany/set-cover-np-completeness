def brute_force(U, S):
    B = [0] * (len(S)+1)                                # O(S+1) 
    C = set()                                           
    temp = len(U)                                       
    count = 0                                           
    while C != U:                                       # O(U)*O(S²)
        for s in S:                                     # O(S)
            index = S.index(s)-1                       
            if temp >= len(s.symmetric_difference(U)) and B[index] == 0: 
                temp = len(s.symmetric_difference(U))  
        B[index] = 1                                   
        C = C.union(S[index])                           # O(S)                      
        S.pop(index)                                                                        
        count += 1                                     
    return B 

#Assumindo que u tenha tamanho n e s tenha tamanho m
#Complexidade Final
#
# O(U)*O(S²) + O(S+1) => O(n*m²) 
#