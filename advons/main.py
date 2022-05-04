class endi:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __and__(self, value):    
        return endi(self.x + value.x, self.y + value.y)
    
    def __repr__(self):    
        return f"X ning qiymati: {self.x} va Y ning qiymati: {self.y}"
    
num1 = endi(10, 10)
num2 = endi(20, 20)
num3 = endi(20, 20)
print(num1 + num2 + num3)
        
      