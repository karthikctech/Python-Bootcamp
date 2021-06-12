# to use itrators using two types of key word 1.iter(to call the function)  2.next(going next step in program)
sk = [2, 3, 4, 5, 5, 6]
for i in sk:
    # print(i)
 sk = iter(sk)


print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))

print("fineshed")

# create own itrators

class Karthik:
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

obj = Karthik(5)
sk = iter(obj)
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))
print(next(sk))

# or
for i in Karthik(5):
    print(i)


