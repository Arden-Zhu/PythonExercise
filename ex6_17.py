def main():
    print('a =', end=' ')
    a = int(input())
    print('b =', end=' ')
    b = int(input())
    common_divisor = min(a, b)
    while not (a % common_divisor == 0 and b % common_divisor == 0):
        common_divisor-=1
    print('common divisor {}'.format(common_divisor))

if __name__ == "__main__":
    main()