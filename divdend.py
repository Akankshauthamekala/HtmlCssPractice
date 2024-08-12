class Demo2:
    def __init__(self,x):
        self.x=x
    def __truediv__(self,other):
        return f"div of{self.x}and{other.x} is:{self.x/other.x}"

d3=Demo2(10)
d4=Demo2(20)
print(d4/d3)
