class Demo1:
    def __init__(self,x):
        self.x=x
    def __mul__(self,other):
        return f"mul of{self.x} and{other.x} is:{self.x*other.x}"

d1=Demo1(10)
d2=Demo1(20)
print(d1*d2)
