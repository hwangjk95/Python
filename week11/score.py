class Score:
    def __init__(self,n,k,e,m):
        self.name = n
        self.kor = k
        self.eng = e
        self.mat = m
        
        
        
    def avg(self):
        return (self.kr + self.eng +self.mat)/3
    
    def __str__(self):
        return f"ÀÌ¸§:{self.name} ±¹¾î:{self.kor} ¿µ¾î:{self.eng} ¼öÇÐ:{self.mat} Æò±Õ:{self.avg():0.2f}"
    
        
        
    def file_content(self):
        return f"{self.name},{self.kor},{self.eng},{self.mat}\n"
    
    if __name__ == "__main__":
        s1 = Score("±èÀÎÇÏ", 100, 90, 80)
        s2 = Score("±è¹ÎÇÏ", 90, 50, 20)
    
    def avg(k, e, m):
        return (k+e+m)/3
    
    print(avg(s1.kor + s1.eng + s1.mat))
    print(avg(s2.kor + s2.eng + s1.mat))
    
    print(s1.avg())
    print(s2.avg())