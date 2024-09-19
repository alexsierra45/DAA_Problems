def solve(A,B,p,k):
    n=max(max(A),max(B))+1
    arr=[]
    for i in range(n):
        arr.append(0)
        if i in A:
            arr[i]+=1
        if i in B:
            arr[i]+=2    
    
    cache = dict()

    def dynamic_solve(i,k_A,k_B,current_p):
        #Previous visited
        if (i,k_A,k_B,current_p) in cache:
            return cache[i,k_A,k_B,current_p]
        
        #Base case
        if i==n:
            cache[i,k_A,k_B,current_p]=0
            return 0

        #Ignore problem
        possible_solutions=[
            dynamic_solve(i+1,max(k_A-1,0),max(k_B-1,0),current_p)
            + (1 if ((k_A!=0 and arr[i] % 2 == 1) or (k_B!=0 and arr[i] >= 2)) 
                else 0)
        ]
        #Look to A
        if current_p>0 and k_A==0  and (arr[i] == 1 or (arr[i]==3 and k_B==0)):
            possible_solutions.append(
                dynamic_solve(i+1,k-1,max(k_B-1,0),current_p-1)+1
            )
        #Look to B
        if current_p>0 and k_B==0  and (arr[i] == 2 or (arr[i]==3 and k_A==0)):
            possible_solutions.append(
                dynamic_solve(i+1,max(k_A-1,0),k-1,current_p-1)+1
            )
        
        cache[i,k_A,k_B,current_p] = max(possible_solutions)

        return cache[i,k_A,k_B,current_p]
    
    return dynamic_solve(0,0,0,p)