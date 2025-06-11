# Find Whether a Number is a Power of Two
def num(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0

n = int(input('Enter a number: '))
if num(n):
    print('{} is a power of two.'.format(n))
else:
    print('{} is not a power of two.'.format(n))
