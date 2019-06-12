solutions = []
state = []

def main():
    n = 3
    k = 2
    solve(n, k)
    print_result()

def solve(n, k):
    if n == 0:
        solutions.append([] + state)
    else:
        state.append(-1)
        for i in range(k):
            state[len(state) - 1] = i
            solve(n-1, k)
        del state[len(state) - 1]

# print result
def print_result():
    for i in range(len(solutions)):
        print("{} : {}".format(i, solutions[i]))

if __name__ == "__main__":
    main()

