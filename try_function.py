a = 'global'

def fun1():
    a = 'out'
    b = [1, 2, 3]
    print(a, b)
    funIn(a, b)
    print(a, b)

def funIn(a, b):
    a = 'in'
    b[1] += 1
    print(a, b)
    b = [4, 5]
    print(a, b)

def fun2():
    print('begin fun2:')
    a = 'global changed in fun2'
    print(a)
    print('end fun2:')

def fun3():
    global a
    a = 'global changed'
    print(a)

def main():
    print(a)
    fun1()
    print(a)
    fun2()
    print(a)
    fun3()    
    print(a)


if __name__ == "__main__":
    main()