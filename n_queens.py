solutions = []
state = []

def main():
    n = 8
    k = 64
    init(n)
    solve(n, k)
    print_result()

def init(n):
    for _ in range(n):
        state.append(-1)

def solve(n, k):
    if n == 0:
        solutions.append([] + state)
    else:
        for i in range(k):
            state[n - 1] = i
            if fit(n - 1):
                solve(n-1, k)

# check if the queen at position pos fits all the others
def fit(pos):
    pass

# print result
def print_result():
    for i in range(len(solutions)):
        print("{} : {}".format(i, solutions[i]))

if __name__ == "__main__":
    main()

