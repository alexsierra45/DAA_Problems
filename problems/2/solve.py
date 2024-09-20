def solve(A, B, p, k):
    n = max(max(A), max(B)) + 1

    # mask_A = [0] * n
    # mask_B = [0] * n
    # mask = [0] * n

    # for problem in A:
    #     mask_A[problem] |= 1
    # for problem in B:
    #     mask_B[problem] |= 1
    # for i in range(n):
    #     mask[i] = mask_A[i] & mask_B[i]

    # solved_A = [0] * n
    # solved_B = [0] * n
    # solved_AND = [0] * n
    # for i in range(0, n):
    #     solved_A[i] += solved_A[i - 1] + mask_A[i]
    #     solved_B[i] += solved_B[i - 1] + mask_B[i]
    #     solved_AND[i] += solved_AND[i - 1] + mask[i]

    # cache = dict()

    # def dynamic_solve(index, a, b, current_p):
    #     # Visited previously
    #     if (index, a, b, current_p) in cache:
    #         return cache[index, a, b, current_p]
        
    #     # Base case
    #     if index == n:
    #         cache[index, a, b, current_p] = 0
    #         return 0
        
    #     # Ignore problem
    #     possible_solutions = [
    #         dynamic_solve(index + 1, max(a - 1, 0), max(b - 1, 0), current_p)
    #     ]

    #     # Take problem in A
    #     if current_p > 0 and a == 0 and mask_A[index]:
    #         possible_solutions.append(
    #             dynamic_solve(index + 1, k - 1, max(b - 1, 0), current_p - 1)
    #             + solved_A[min(index + k - 1, n - 1)] - (0 if index == 0 else solved_A[index - 1])
    #             - (0 if b == 0 else (solved_AND[min(index + b - 1, n - 1)] - (0 if index == 0 else solved_AND[index - 1])))
    #         )

    #     # Take problem in B
    #     if current_p > 0 and b == 0 and mask_B[index]:
    #         possible_solutions.append(
    #             dynamic_solve(index + 1, max(a - 1, 0), k - 1, current_p - 1)
    #             + solved_B[min(index + k - 1, n - 1)] - (0 if index == 0 else solved_B[index - 1])
    #             - (0 if a == 0 else (solved_AND[min(index + a - 1, n - 1)] - (0 if index == 0 else solved_AND[index - 1])))
    #         )

    #     cache[index, a, b, current_p] = max(possible_solutions)

    #     return cache[index, a, b, current_p]

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
    
    return dynamic_solve(0, 0, 0, p)