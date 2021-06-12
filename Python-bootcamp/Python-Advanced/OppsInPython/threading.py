import _thread
import time
# multi treading is used to execute all function at a sme time

def a():
    count = 0
    while count <= 5:
        count += 1
        time.sleep(3)
        print("hello dark")
def b():
    count = 0
    while count <= 5:
        count += 1
        time.sleep(2)
        print("hello dark world")


try :
     _thread.start_new_thread(a, ( ))    
     _thread.start_new_thread(b, ())  
except:
    print("error occur in treading")

while 1:
    pass
