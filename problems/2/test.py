import random
import itertools
import solve

MAX_N=20
MAX_P=5
MAX_K=6

def build_test():
    global MAX_N
    global MAX_P
    global MAX_K

    A=[i for i in range(MAX_N) if random.randint(0,1)==1]
    B=[i for i in range(MAX_N) if random.randint(0,1)==1]
    
    p=random.randint(1,MAX_P)
    k=random.randint(1,MAX_K)

    return (A,B,p,k)

def get_solutions(A,B,p):
    if len(A)+len(B)<=p:
        return [(a,'A') for a in A]+[(b,'B') for b in B]
    return list(itertools.combinations(
        [(a,'A') for a in A]+[(b,'B') for b in B], p)
    )

def try_solve(solution, A, B, k):
    answers=set()
    for k_i in range(k):
        for a_i, char in solution:
            if a_i+k_i in (A if char=='A' else B):
                answers.add(a_i+k_i)
    return len(answers)

def solve_test(A, B, p, k):
    best=0
    for solution in get_solutions(A.copy(),B.copy(),p):
        best=max(try_solve(solution,A,B,k),best)
    return best

for i in range(100):
    test=build_test()
    fb=solve_test(test[0],test[1],test[2],test[3])
    ds=solve.solve(test[0],test[1],test[2],test[3])
    if fb!=ds:
        print("Error en test ",i)
        print(test)
        print(fb,ds)
        break