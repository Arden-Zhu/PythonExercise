solutions = []
state = []

def main():
    n = 8
    init(n)
    solve(n - 1, n)
    print_result()

def init(n):
    for _ in range(n):
        state.append(-1)

def solve(c, n):
    if c < 0:
        solutions.append([] + state)
    else:
        for i in range(n * c, n * c + n):
            state[c] = i
            if test(c, n):
                solve(c-1, n)

# check if the queen at position pos fits all the others state[pos] vs state[pos + 1:]
def test(pos, n):
    x1 = state[pos] % n
    y1 = state[pos] // n
    for pos2 in range(pos + 1, n):
        x2 = state[pos2] % n
        y2 = state[pos2] // n
        if x1 == x2 or y1 == y2 or x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
            return False
    return True


# print result
def print_result():
    for i in range(len(solutions)):
        print("{} : {}".format(i, solutions[i]))

if __name__ == "__main__":
    main()

