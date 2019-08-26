# defining function
def fuc(x):
    return x**2 - 4

# Defining inputs
num_iter = 100
req_iter = 0
tol = 10**(-4)
a = 0
b = 3
fa = fuc(a)
fb = fuc(b)

# Ensuring that f(a) and f(b) have different signs
if fa*fb < 0:
    # applying bisection algorithm
            for i in range(0, num_iter):
                p = a + (b-a)/2
                if (b - a) / 2 <= tol or fuc(p) == 0:
                    req_iter = i + 1
                    print(f"number of iterations used: {req_iter}")
                    print(f"p = {p}")
                    print(f"f(p) = {fuc(p)}")
                    break
                elif fa*fuc(p) < 0:
                    b = p
                else:
                    a = p
                if i == num_iter - 1 and (b-a)/2 > tol:
                    print(f"The procedure could not achieve the tolerance level at N = {num_iter}")
else:
    print(f"Bisection method cannot be applied because f(a) ({fa}) and f(b) ({fb}) don't have the same sign")

