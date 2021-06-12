def fact (n):
    f = 1
    for i in  range(1, n + 1):
        k = f * i
        print (k)
        n = 5
        result = fact(n)
        print(result)
fact(5)
