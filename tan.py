class Fraction:
    def __init__(self,n,m):

        self.top = n
        self.bottom = m

    

    def __str__(self) -> str:
        return str(self.top)+"/"+ str(self.bottom)
    
    def __add__(self,other):
        newtop = self.top * other.bottom + other.top * self.bottom
        newbottom = self.bottom * other.bottom

        print(Fraction(newtop,newbottom))
        return(Fraction(newbottom,newtop))                                                                                                                                                                                                                                                                                                                                                                                                         
    

myfraction = Fraction(4,10)
otherfraction = Fraction(3,8)
f3 = myfraction + otherfraction
f4 = otherfraction + myfraction
k = myfraction.__str__()
print(k)
print(str(otherfraction))
print(f4)
print(f3)

