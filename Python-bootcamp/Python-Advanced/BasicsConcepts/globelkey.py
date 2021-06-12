# global variable
s =15
# local variable
def secret():
    s = 5
    print(f"local variable is : {s}")
secret()
print("global value is ", s)
#to change global variable without changing lv
 
s = 15
def think():
     global s
     k = 5
     print(f"local scope is: {k}")
think()
print(f"global scope: {s}")

