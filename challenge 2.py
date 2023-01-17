class calculator():
    def __init__(self, a,b):
     self.a=a
     self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    obj=calculator(10,94)
    obj.add()
    obj.multiply()
    obj.div()
    obj.substraction()
print()