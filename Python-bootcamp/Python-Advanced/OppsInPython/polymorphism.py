# function overloading

# in python does not access directly function overloading
 
class demo():
    def sum(self, a = None, b= None, c= None):
        if a != None and b != None and c != None:
            d= a + b + c
            print(d)
        elif a != None and b != None:
            d = a + b
            print(d)
        else:
            d = a
            print(d)
obj = demo()
ans = obj.sum(12, 2, 5)
print(f"your answer is {ans}")

# function overridding is used to specify the lass class outbut for ex : given below

class demo():
    def fun(self):
      print("welcome")
class demo1(demo):
    def fun(self):
      print("hello world")
obj = demo1()
obj.fun()





