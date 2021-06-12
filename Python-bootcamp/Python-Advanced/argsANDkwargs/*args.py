# *args is the most useful key word let see how it is works *is the important it is a tuple type

def add(*args):
    for i in args:
        print(i)
add(10+ 20 + 30 + 40 + 50)

# OR

def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(add(10, 20, 30, 40, 50))

