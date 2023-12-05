"""
class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+":"+self.meaning
l1=[]
while(True):
    w=input("Enter the word:")
    m=input("Enter the meaning:")
    o=flashcards(w,m)
    l1.append(o.__str__())
    d=input("press y to enter more flashcards:").lower()
    if(d!='y'):
        break)
print(l1)
"""

"""
class shape:
    def area(self):
        pass
    def perimeter(self):
        print("perimeter")
class circle(shape):
    def _init_(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2
    def perimeter(self):
        return 2*3.14*self.r
obj1=circle(3)
print(obj1.area(),obj1.perimeter()) 
"""

class shoppingcart:


