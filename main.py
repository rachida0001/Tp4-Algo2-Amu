def suite_Fibonacci(n):
    yield  1
    yield  1
    F =   [1,1]
    for i in range(2,n):
        yield F[i-1]+F[i-2]
        F.append(F[i-1]+F[i-2])
     

def super_impair(k):
    return not bool([int(i) for i in str(k) if int(i)%2 ==0])

def expression_generatrice(n):
    return (x for x in suite_Fibonacci(n) if super_impair(x))

for x in suite_Fibonacci(5):
    print(x)
    
print(super_impair(113))

for i in expression_generatrice(10):
    print(i)
    
print(expression_generatrice(10))