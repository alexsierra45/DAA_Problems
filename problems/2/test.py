import random
import itertools
from solve import solve

MAX_N = 25
MAX_P = 5
MAX_K = 6

def generate_case():
    global MAX_N
    global MAX_P
    global MAX_K

    A=[i for i in range(MAX_N) if random.randint(0, 1) == 1]
    B=[i for i in range(MAX_N) if random.randint(0, 1) == 1]
    
    p = random.randint(1, MAX_P)
    k = random.randint(1, MAX_K)

    if len(A) == 0 or len(B) == 0:
        return generate_case()
    return (A, B, p, k)

def solve_test(A, B, p, k):
    best = 0

    if len(A) + len(B) <= p:
        ans = set()
        for a in A:
            ans.add(a)
        for b in B:
            ans.add(b)

        return len(ans)

    def get_combinations():
        return list(itertools.combinations(
            [(a, 'A') for a in A] + [(b, 'B') for b in B], p))

    def try_solve(solution):
        answers = set()
        for k_i in range(k):
            try:
                for a_i, char in solution:
                    if a_i+k_i in (A if char == 'A' else B):
                        answers.add(a_i + k_i)
            except:
                a_i, char = solution
                if a_i+k_i in (A if char == 'A' else B):
                    answers.add(a_i + k_i)

        return len(answers)
    
    for solution in get_combinations():
        try:
            best = max(try_solve(solution), best)
        except:
            print(solution)
        best = max(try_solve(solution), best)

    return best

def generate_test(num):
    tests = []
    for _ in range(num):
        case = generate_case()
        tests.append((case, solve_test(case[0], case[1], case[2], case[3])))
    accuracy = 0
    for case, ans in tests:
        solution = solve(case[0], case[1], case[2], case[3])
        if solution == ans:
            accuracy += 1
        else:
            print(f'Error in test {case}')
            print(f'Solution: {solution}, expected solution: {ans}')

    plural = '' if num == 1 else 's'
    print(f'Accuracy of {accuracy / num * 100}% for {num} test{plural} case{plural}')

generate_test(100)