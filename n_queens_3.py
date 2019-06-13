def main():
    queen = Queen(4)
    queen.solve()
    queen.print_result()

class Queen(object):
    def __init__(self, n):
        self.n = n
        self.k = n * n
        self.solutions = []
        self.initState()

    def initState(self):
        self.state = []
        for _ in range(self.n):
            self.state.append(-1)

    def solve(self, c = None):
        if (c == None):
            c = self.n - 1

        if c < 0:
            self.solutions.append([] + self.state)
        else:
            for i in range(self.n * c, self.n * (c + 1)):
                self.state[c] = i
                if self.test(c):
                    self.solve(c-1)

    # check if the queen at position pos fits all the others state[pos] vs state[pos + 1:]
    def test(self, pos):
        x1 = self.state[pos] % self.n
        y1 = self.state[pos] // self.n
        for pos2 in range(pos + 1, self.n):
            x2 = self.state[pos2] % self.n
            y2 = self.state[pos2] // self.n
            if x1 == x2 or y1 == y2 or x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
                return False
        return True


    # print result
    def print_result(self):
        for i in range(len(self.solutions)):
            print("{} : {}".format(i, self.solutions[i]))

if __name__ == "__main__":
    main()

