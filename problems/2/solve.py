import math

def solve_base_dynamic(A, B, p, k):
    n = max(max(A), max(B)) + 1

    mask_A = [0] * n
    mask_B = [0] * n

    for problem in A:
        mask_A[problem] |= 1
    for problem in B:
        mask_B[problem] |= 1

    cache = dict()

    for i in range(n,-1,-1):
        for p_i in range(p+1):
            for k_a in range(k):
                for k_b in range(k):
                    if i == n:
                        cache[i,k_a,k_b,p_i]=0
                        continue

                    if i==3 and k_a==0 and k_b==k-1 and p==p_i-1:
                        print()
                    # Ignore problem
                    plus_1 = (mask_A[i] == 1 and k_a > 0) or (mask_B[i] == 1 and k_b > 0) 
                    possible_solutions = [
                        cache[i+1, max(k_a-1,0), max(k_b-1,0), p_i] + (1 if plus_1 else 0)
                    ]

                    if p_i > 0:
                        # Take problem in A
                        possible_solutions.append(
                            cache[i+1, k-1, max(k_b-1,0), p_i-1] + mask_A[i]
                        )
                        # Take problem in B
                        possible_solutions.append(
                            cache[i+1, max(k_a-1,0), k-1, p_i-1] + mask_B[i]
                        )
                    
                    if p_i > 2:
                        # Take problem in both A and B
                        possible_solutions.append(
                            cache[i+1, k-1, k-1, p_i-2] + (mask_A[i] & mask_B[i])
                        )
                    
                    cache[i, k_a, k_b, p_i]= max(possible_solutions)

    return cache[0, 0, 0, p]

def solve_with_shortcuts(A, B, p, k):
    n = max(max(A), max(B)) + 1

    mask_A = [0] * n
    mask_B = [0] * n

    for problem in A:
        mask_A[problem] |= 1
    for problem in B:
        mask_B[problem] |= 1

    rest = [0] * n
    rest[-1] = mask_A[-1] | mask_B[-1]
    for i in range(n-2, -1, -1):
        rest[i] = rest[i+1] + (mask_A[i] | mask_B[i])

    cache = dict()

    def recursive_solve(i, k_a, k_b, current_p):
        # Visited previously
        if (i, k_a, k_b, current_p) in cache:
            return cache[i, k_a, k_b, current_p]
        
        # Base cases
        if i == n or (current_p == 0 and k_a == 0 and k_b==0):
            cache[i, k_a, k_b, current_p] = 0
            return 0
        
        # case when you can solve the rest of the problem
        if math.ceil( (n - i - k_a + 1) / k ) + math.ceil( ( n - i - k_b + 1 ) / k) < current_p:
            cache[i, k_a, k_b, current_p] = rest[i]
            return cache[i, k_a, k_b, current_p]

        # Ignore problem
        possible_solutions = [
            recursive_solve(i + 1, max(k_a - 1, 0), max(k_b - 1, 0), current_p)
            + (1 if (mask_A[i] == 1 and k_a > 0) or (mask_B[i] == 1 and k_b > 0) else 0)
        ]

        # Take problem in A
        if current_p > 0 and k_a == 0 and mask_A[i]:
            possible_solutions.append(
                recursive_solve(i + 1, k-1, max(k_b - 1, 0), current_p - 1) + 1
            )

        # Take problem in B
        if current_p > 0 and k_b == 0 and mask_B[i]:
            possible_solutions.append(
                recursive_solve(i + 1, max(k_a - 1, 0), k-1, current_p - 1) + 1
            )

        cache[i, k_a, k_b, current_p] = max(possible_solutions)

        return cache[i, k_a, k_b, current_p]

    return recursive_solve(0, 0, 0, p)

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