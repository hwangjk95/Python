class Score:
    def __init__(self,name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        
    def avg(self):
        return (self.kor+self.eng+self.mat)/3
    def __str__(self):
        return f"이름:{self.name} 국어:{self.kor} 영어:{self.eng} " \
        f"수학:{self.mat} 평균:{self.avg():0.2f}"

    def file_content(self):
        return f"{self.name},{self.kor},{self.eng},{self.mat}\n"