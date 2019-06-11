def main():
    print('a =', end=' ')
    a = int(input())
    print('b =', end=' ')
    b = int(input())
    print('GCD({} , {}) = {}'.format(a, b, gcd(a, b)))
    print('LCM({} , {}) = {}'.format(a, b, int(a * b / gcd(a, b))))

def gcd(a, b):
    common_divisor = min(a, b)
    while not (a % common_divisor == 0 and b % common_divisor == 0):
        common_divisor-=1
    return common_divisor

if __name__ == "__main__":
    main()