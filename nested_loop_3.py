solutions = []
state = []

def main():
    n = 3
    k = 2
    init(n)
    solve(n, k)
    print_result()

def init(n):
    for _ in range(n):
        state.append(-1)

def solve(n, k):
    c = n  - 1
    while True:
        if c < 0:
            solutions.append([] + state)
            c += 1
        elif c == n:
            break
        else:
            if state[c] + 1 < k:
                state[c] += 1
                c -= 1
            else:
                state[c] = -1
                c += 1

# print result
def print_result():
    for i in range(len(solutions)):
        print("{} : {}".format(i, solutions[i]))

if __name__ == "__main__":
    main()

