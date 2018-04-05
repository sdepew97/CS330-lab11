# fibr(n) - Compute the nth Fibonacci number, recursively
def fibr(n):
    if n==1 or n==2:
        return 1
    else:
        return fibr(n-2) + fibr(n-1)

