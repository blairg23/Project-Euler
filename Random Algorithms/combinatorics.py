def C(N, n):
    """Combinations"""
    return math.factorial(N) / (math.factorial(n)*math.factorial(N-n))

def P(N, n):
    """Permutations"""
    return math.factorial(N) / math.factorial(N-n)


N = 5
n = 2

print C(N,n)
print P(N,n)
