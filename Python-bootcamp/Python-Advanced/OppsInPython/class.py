class karthik:
    print('hello world')
    s = 55
    def secret(self, a, b):
# self key is used to add the variable outside of function are also
        c = a + b + self.s
        print(c)
   
obj = karthik()
obj.secret(10, 5)