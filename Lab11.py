# fibr(n) - Compute the nth Fibonacci number, recursively
def fibr(n):
    if n==1 or n==2:
        return 1
    else:
        return fibr(n-2) + fibr(n-1)

# fibi(n) - Compute the nth Fibonacci number, iteratively
def fibi(n):
    if n==1 or n==2:
        return 1
    fibMinus2 = 1
    fibMinus1 = 1
    i = 3
    while(i <= n):
        fibI = fibMinus2 + fibMinus1
        fibMinus2 = fibMinus1
        fibMinus1 = fibI
        i = i + 1
    return fibI

# fibg() - A generator for Fibonacci sequence
def fibg():
    fibMinus2 = 1
    fibMinus1 = 1

    while True:
        fibOld = fibMinus2
        fibI = fibMinus2 + fibMinus1
        fibMinus2 = fibMinus1
        fibMinus1 = fibI

        if fibOld > 6000000:
            raise StopIteration

        yield fibOld

# fibg2() - A generator for Fibonacci sequence
def fibg2(n):
    fibMinus2 = 1
    fibMinus1 = 1
    fibN = 0

    while True:
        fibOld = fibMinus2
        fibI = fibMinus2 + fibMinus1
        fibMinus2 = fibMinus1
        fibMinus1 = fibI
        fibN += 1

        if fibN > n:
            raise StopIteration

        yield fibOld

# isPrime(number) - A method to check if a number is prime or not
def isPrime(number):
    if number > 1:
        if number == 2:
            return True

        elif number != 2:
            for i in range(2, number):
                if number % i == 0:
                    return False
                elif number % i != 0 and i >= number/2:
                    return True
        return False
    return False

# prime(n) - A generator for prime numbers
def prime(n):
    primeN = 1
    numberToCheck = 2
    
    while True:
        if(isPrime(numberToCheck)):
            primeN += 1
            yield numberToCheck
            numberToCheck += 1
        
        else:
            numberToCheck += 1

        if primeN > n:
            raise StopIteration
        
def main():
    # print("Recursive Implementation:")
    # print(">>>" + str(fibr(20)))
    # print(">>>" + str(fibr(30)))
    # print(">>>" + str(fibr(40)))
    # # print(">>>" + str(fibr(50)))
    #
    # print("Iterative Implementation:")
    # print(">>>" + str(fibi(20)))
    # print(">>>" + str(fibi(30)))
    # print(">>>" + str(fibi(40)))
    # print(">>>" + str(fibi(50)))
    # print(">>>" + str(fibi(60)))

    x = 1
    for i in prime(100):
        print(x, ":" , i)
        x += 1

main()
