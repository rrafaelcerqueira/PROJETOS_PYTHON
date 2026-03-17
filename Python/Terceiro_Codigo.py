lista = list(range(1,101))

def fizzbuzz(numero):
    if numero %3 == 0:
        return 'Fizz'
    if numero %5 == 0:
        return 'Buzz'
    else:
        return 1

assert fizzbuzz(1) == 1
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(6) == 'Fizz'
