class hello():
    print('welcome')
    # to create constructor using __init__ function
    def __init__(self):
        self.Name = "KARTHIK"
        self.Age = 20

    def display(self):
        print("name is : ",self.Name)
        print("age is : ",self.Age)
obj = hello()
obj.display()