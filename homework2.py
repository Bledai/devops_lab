def word(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

def gcd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def restr(s):
    s = list(map(int, s.split()))
    return s


if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print(word(i))
    s = restr(input())
    print('GCD %s and %s : %s' % (s[0], s[1], gcd(s[0], s[1])))
