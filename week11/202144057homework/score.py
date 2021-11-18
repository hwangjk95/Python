class Score:
    def __init__(self,n,k=0,e=0,m=0):
        self.name = n
        self.kor = k
        self.eng = e
        self.mat = m
        
        
        
    def avg(self):
        return (self.kor + self.eng +self.mat)/3
    
    def __str__(self):
        return f"이름:{self.name} 국어:{self.kor} 영어:{self.eng} 수학:{self.mat} 평균:{self.avg():0.2f}"
    
        
        
    def file_content(self):
        return f"{self.name},{self.kor},{self.eng},{self.mat}\n"
    
