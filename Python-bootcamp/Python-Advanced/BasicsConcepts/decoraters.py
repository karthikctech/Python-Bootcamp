# decoraters is used to modify the code without changing any line code for example:
def add (a, b):
    print(a + b)

def smart_add(kar):
    def inner(a, b):
       a, b = b, a
       return kar(a, b)
    return inner
add = smart_add(add) "this line is a decorders"
add (15, 5)